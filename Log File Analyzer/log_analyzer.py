#!/usr/bin/env python3
"""
Professional Log Analyzer

This script parses a web server log file (Apache/Nginx),
analyzes key metrics such as top IPs, top URLs, total requests,
and 404 errors, and generates a summary report.

Features:
- Command-line interface for log file, report file, and top N.
- Logging to file and console with proper formatting.
- Robust error handling for real-world usage.

Dependencies:
- config.py
- log_parser.py
- log_reporter.py
"""

import os
import sys
import argparse
import logging
from collections import Counter
from typing import List, Dict, Any

from config import LOG_FILE_PATH, LOG_OUTPUT_FILE, SUMMARY_REPORT_FILE, TOP_COUNT
from log_parser import parse_log_line
from log_reporter import generate_report


# ------------------------------
# Logging Setup
# ------------------------------
def setup_logging(log_file: str) -> None:
    """
    Set up logging to file and console.

    Args:
        log_file (str): Path to the log file for logging.
    """
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Avoid duplicate handlers
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    logger.addHandler(console_handler)


# ------------------------------
# Log Parsing
# ------------------------------
def parse_log(file_path: str) -> List[Dict[str, Any]]:
    """
    Parse log file and extract entries.

    Args:
        file_path (str): Path to the log file.

    Returns:
        List[Dict[str, Any]]: List of parsed log entries.
    """
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


# ------------------------------
# Log Analysis
# ------------------------------
def analyze_logs(entries: List[Dict[str, Any]], top_count: int) -> Dict[str, Any]:
    """
    Analyze log entries for key metrics.

    Args:
        entries (List[Dict[str, Any]]): Parsed log entries.
        top_count (int): Number of top URLs/IPs to include.

    Returns:
        Dict[str, Any]: Summary statistics.
    """
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


# ------------------------------
# CLI Argument Parser
# ------------------------------
def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed CLI arguments.
    """
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


# ------------------------------
# Main Function
# ------------------------------
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


# ------------------------------
# Entry Point
# ------------------------------
if __name__ == "__main__":
    main()
