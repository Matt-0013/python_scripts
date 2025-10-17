import os
import tarfile
import logging
from datetime import datetime
import paramiko
from scp import SCPClient
from config import SOURCE_DIR, BACKUP_DIR, REMOTE_HOST, REMOTE_PORT, USERNAME, SSH_KEY_PATH, REMOTE_DIR

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename='logs/backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def create_backup():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"backup_{timestamp}.tar.gz"
    backup_path = os.path.join(BACKUP_DIR, backup_filename)

    try:
        os.makedirs(BACKUP_DIR, exist_ok=True)
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
        logging.info(f"Backup created successfully: {backup_path}")
        print(f"[INFO] Backup created: {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        print(f"[ERROR] Failed to create backup: {e}")
        return None

def send_to_remote(file_path):
    if file_path is None:
        return False

    try:
        key = paramiko.RSAKey.from_private_key_file(SSH_KEY_PATH)

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=REMOTE_HOST,
            port=REMOTE_PORT,
            username=USERNAME,
            pkey=key
        )

        with SCPClient(ssh.get_transport()) as scp:
            scp.put(file_path, REMOTE_DIR)

        ssh.close()
        logging.info(f"Backup transferred successfully to {REMOTE_HOST}:{REMOTE_DIR}")
        print(f"[INFO] Backup transferred successfully to {REMOTE_HOST}:{REMOTE_DIR}")
        return True

    except Exception as e:
        logging.error(f"Failed to transfer backup: {e}")
        print(f"[ERROR] Failed to transfer backup: {e}")
        return False

def main():
    backup_file = create_backup()
    success = send_to_remote(backup_file)

    if success:
        logging.info(f"Backup operation SUCCESS: {backup_file}")
    else:
        logging.error(f"Backup operation FAILED: {backup_file}")


if __name__ == "__main__":
    main()

