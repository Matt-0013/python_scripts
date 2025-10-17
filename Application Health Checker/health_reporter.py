import os
import logging
from datetime import datetime
from typing import List, Dict
from config import HEALTH_REPORT_FILE


def generate_health_report(health_summary: List[Dict[str, str]]) -> None:

    os.makedirs(os.path.dirname(HEALTH_REPORT_FILE), exist_ok=True)

    report_lines = [
        "===== Application Health Report =====",
        f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Application Status Summary:"
    ]

    for app in health_summary:
        status_icon = "✅" if app['status'] == 'up' else "❌"
        report_lines.append(
            f"{status_icon} {app['url']} - Status: {app['status'].upper()} "
            f"(HTTP {app['http_code']}) Checked at: {app['checked_at']}"
        )

    report_lines.append("===============================")

    report_text = "\n".join(report_lines)

    try:
        with open(HEALTH_REPORT_FILE, "w") as f:
            f.write(report_text)
        logging.info(f"Health report generated: {HEALTH_REPORT_FILE}")
    except Exception as e:
        logging.error(f"Failed to write health report: {e}")

