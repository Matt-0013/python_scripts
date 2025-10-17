import os
import tarfile
import logging
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from config import (
    SOURCE_DIR,
    BACKUP_DIR,
    S3_BUCKET,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION
)


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
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(SOURCE_DIR, arcname=os.path.basename(SOURCE_DIR))
        logging.info(f"Backup created successfully: {backup_path}")
        print(f"[INFO] Backup created: {backup_path}")
        return backup_path
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        print(f"[ERROR] Failed to create backup: {e}")
        return None


def upload_to_s3(file_path):
    if file_path is None:
        return False

    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    try:
        file_name = os.path.basename(file_path)
        s3_client.upload_file(file_path, S3_BUCKET, file_name)
        logging.info(f"Backup uploaded successfully to S3: s3://{S3_BUCKET}/{file_name}")
        print(f"[INFO] Backup uploaded successfully to S3: s3://{S3_BUCKET}/{file_name}")
        return True

    except FileNotFoundError:
        logging.error(f"The file {file_path} was not found.")
        print(f"[ERROR] The file {file_path} was not found.")
        return False

    except NoCredentialsError:
        logging.error("AWS credentials not available.")
        print("[ERROR] AWS credentials not available.")
        return False

    except ClientError as e:
        logging.error(f"Failed to upload to S3: {e}")
        print(f"[ERROR] Failed to upload to S3: {e}")
        return False

def main():
    backup_file = create_backup()
    success = upload_to_s3(backup_file)

    if success:
        logging.info(f"S3 backup operation SUCCESS: {backup_file}")
    else:
        logging.error(f"S3 backup operation FAILED: {backup_file}")


if __name__ == "__main__":
    main()
