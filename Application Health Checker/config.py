from pathlib import Path

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

REQUEST_TIMEOUT = 5  
MAX_RETRIES = 2      

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
HEALTH_LOG_FILE = LOG_DIR / "health_check.log"

REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)
HEALTH_REPORT_FILE = REPORT_DIR / "health_report.txt"
TOP_FAILURES_COUNT = 5  
LOG_FILE_PATH = HEALTH_LOG_FILE
REPORT_FILE_PATH = HEALTH_REPORT_FILE

