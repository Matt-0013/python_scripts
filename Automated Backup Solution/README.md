A Python-based solution to automate backups locally, to remote servers via SCP, and to AWS S3.

Features

- Create compressed backups (`.tar.gz`) of a specified folder.
- Upload backups to AWS S3 using `boto3`.
- Transfer backups to remote servers via SCP using `paramiko`.
- Maintain logs for all backup operations.


Clone the repository:

git clone https://github.com/Matt-0013/python_scripts
cd Automated\ Backup\ Solution


Install dependencies:

pip install -r requirements.txt

Configuration

All configurable parameters are in config.py:

SOURCE_DIR: Folder to back up.

BACKUP_DIR: Local backup storage directory.

REMOTE_HOST, REMOTE_PORT, USERNAME, SSH_KEY_PATH, REMOTE_DIR: Remote server details for SCP backup.

S3_BUCKET, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION: AWS S3 credentials and bucket.

Usage
Local + S3 Backup
python cloud_backup.py

Local + Remote Backup via SCP
python remote_backup.py

Output

Logs: Stored in logs/backup.log.

Backups: Stored in backups/ locally.

S3 Backups: Uploaded to the configured S3 bucket.

Remote Backups: Transferred to the remote server directory.