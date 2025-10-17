import os
import sys
import argparse
import logging
from collections import Counter
from typing import List, Dict, Any

from config import LOG_FILE_PATH, LOG_OUTPUT_FILE, SUMMARY_REPORT_FILE, TOP_COUNT
from log_parser import parse_log_line
from log_reporter import generate_report

def setup_logging(log_file: str) -> None:

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)


    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    logger.addHandler(console_handler)


def parse_log(file_path: str) -> List[Dict[str, Any]]:

    if not os.path.exists(file_path):
        logging.error(f"Log file not found: {file_path}")
        return []

    log_entries: List[Dict[str, Any]] = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                entry = parse_log_line(line)
                if entry:
                    log_entries.append({
                        "ip": entry.get("ip", ""),
                        "status": entry.get("status", ""),
                        "url": entry.get("url", "")
                    })
    except Exception as e:
        logging.exception(f"Failed to read log file: {e}")

    return log_entries


def analyze_logs(entries: List[Dict[str, Any]], top_count: int) -> Dict[str, Any]:

    total_requests = len(entries)
    errors_404 = sum(1 for e in entries if e['status'] == '404')

    ip_counter = Counter(e['ip'] for e in entries if e['ip'])
    url_counter = Counter(e['url'] for e in entries if e['url'])

    summary = {
        "total_requests": total_requests,
        "404_errors": errors_404,
        "top_ips": ip_counter.most_common(top_count),
        "top_urls": url_counter.most_common(top_count)
    }

    logging.info(f"Analysis Summary: {summary}")
    return summary


def parse_arguments() -> argparse.Namespace:

    parser = argparse.ArgumentParser(description="Web Log Analyzer")
    parser.add_argument(
        "-l", "--logfile", type=str, default=LOG_FILE_PATH,
        help="Path to web server log file (default from config)."
    )
    parser.add_argument(
        "-o", "--output", type=str, default=SUMMARY_REPORT_FILE,
        help="Path to save summary report (default from config)."
    )
    parser.add_argument(
        "-t", "--top", type=int, default=TOP_COUNT,
        help="Number of top URLs/IPs to display in report (default from config)."
    )
    parser.add_argument(
        "-v", "--log", type=str, default=LOG_OUTPUT_FILE,
        help="Path to log file for analysis process (default from config)."
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    setup_logging(args.log)
    logging.info("Starting log analysis...")

    entries = parse_log(args.logfile)

    if not entries:
        logging.warning("No valid log entries found.")
        print("[INFO] No valid log entries found.")
        return

    summary = analyze_logs(entries, args.top)

    try:
        generate_report(summary, args.output)
        logging.info(f"Summary report generated: {args.output}")
    except Exception as e:
        logging.exception(f"Failed to generate summary report: {e}")

    logging.info("Log analysis completed successfully.")


if __name__ == "__main__":
    main()
