import os
import logging
import requests
import argparse
from datetime import datetime
from typing import Tuple, List

from config import REQUEST_TIMEOUT, HEALTH_LOG_FILE, URLS_TO_MONITOR
from health_reporter import generate_health_report


def setup_logging(log_file: str) -> None:
    
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
        logger.addHandler(console_handler)


def check_application(url: str) -> Tuple[str, int]:
    
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        status = "up" if response.status_code == 200 else "down"
        return status, response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Health check failed for {url}: {e}")
        return "down", 0


def main(urls: List[str]) -> None:
    setup_logging(HEALTH_LOG_FILE)
    logging.info("🚀 Starting application health check...")

    health_summary = []

    for url in urls:
        status, code = check_application(url)
        logging.info(f"Checked {url}: {status.upper()} (HTTP {code})")
        health_summary.append({
            "url": url,
            "status": status,
            "http_code": code,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    generate_health_report(health_summary)
    logging.info("✅ Health check completed successfully.")
    logging.info(f"📄 Report generated: {os.path.abspath('reports/health_report.txt')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Application Health Checker")
    parser.add_argument("--url", help="Check health of a specific URL")
    parser.add_argument("--all", action="store_true", help="Check all URLs from config.py")

    args = parser.parse_args()

    if args.url:
        urls_to_check = [args.url]
    elif args.all:
        urls_to_check = URLS_TO_MONITOR
    else:
        print("⚠️  No URL provided. Use --url <url> or --all to check all configured URLs.")
        exit(1)

    main(urls_to_check)
