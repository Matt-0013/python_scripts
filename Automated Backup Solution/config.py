import os

SOURCE_DIR = "/home/sai/python_scripts/Automated Backup Solution/test_folder"

BACKUP_DIR = os.path.join(os.getcwd(), "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)


REMOTE_HOST = "54.158.62.126"
REMOTE_PORT = 22
USERNAME = "ubuntu"
SSH_KEY_PATH = os.path.expanduser("~/.ssh/demo_backup.pem")
REMOTE_DIR = "/home/ubuntu/backups"
PASSWORD = None  


S3_BUCKET = "automated-backup-demo"
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION = "us-east-1" 
