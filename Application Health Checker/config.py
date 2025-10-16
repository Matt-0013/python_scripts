# config.py
"""
Configuration file for Application Health Checker.

Contains all URLs to monitor, logging settings, request timeouts, and report paths.
"""

from pathlib import Path

# ------------------------------
# URLs to Check
# ------------------------------
URLS_TO_MONITOR = [
    "https://example.com",
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com",
    "https://wikipedia.org",
    "https://python.org",
    "https://reddit.com",
    "https://medium.com",
    "https://aws.amazon.com",
    "https://azure.microsoft.com",
    "https://cloud.google.com",
    "https://linkedin.com",
    "https://twitter.com",
    "https://facebook.com",
    "https://youtube.com",
    "https://npmjs.com",
    "https://pypi.org",
    "https://docker.com",
    "https://kubernetes.io",
    "https://nginx.org",
]

# ------------------------------
# HTTP Request Settings
# ------------------------------
REQUEST_TIMEOUT = 5  # seconds
MAX_RETRIES = 2      # Number of retries for failed requests

# ------------------------------
# Logging Configuration
# ------------------------------
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
HEALTH_LOG_FILE = LOG_DIR / "health_check.log"

# ------------------------------
# Report Configuration
# ------------------------------
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)
HEALTH_REPORT_FILE = REPORT_DIR / "health_report.txt"
TOP_FAILURES_COUNT = 5  # How many top failures to show in report
LOG_FILE_PATH = HEALTH_LOG_FILE
REPORT_FILE_PATH = HEALTH_REPORT_FILE
