# config.py

import os

# ------------------------------
# Source Directory to Back Up
# ------------------------------
SOURCE_DIR = "/home/sai/python_scripts/Automated Backup Solution/test_folder"
#SOURCE_DIR = "/mnt/c/Users/saiar/Downloads/P2"

# ------------------------------
# Local Backup Storage
# ------------------------------
BACKUP_DIR = os.path.join(os.getcwd(), "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)

# ------------------------------
# Remote Server Backup Config
# ------------------------------
REMOTE_HOST = "54.158.62.126"
REMOTE_PORT = 22
USERNAME = "ubuntu"
SSH_KEY_PATH = os.path.expanduser("~/.ssh/demo_backup.pem")
REMOTE_DIR = "/home/ubuntu/backups"
PASSWORD = None  # leave as None because we are using key

# ------------------------------
# AWS S3 Backup Config
# ------------------------------
S3_BUCKET = "automated-backup-demo"
AWS_ACCESS_KEY_ID = "AKIA4553A6AP2OJSTDG5"
AWS_SECRET_ACCESS_KEY = "jIl3z+niaUoyUfMpjTrQODRuzFmfallA14JFQ+Ok"
AWS_REGION = "us-east-1"  # Change to your bucket region
