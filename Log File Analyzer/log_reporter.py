from datetime import datetime
from typing import Dict, Any, List

def generate_report(summary: Dict[str, Any], output_file: str) -> None:
    total_requests: int = summary.get("total_requests", 0)
    errors_404: int = summary.get("404_errors", 0)
    top_urls: List[tuple] = summary.get("top_urls", [])
    top_ips: List[tuple] = summary.get("top_ips", [])

    report_lines: List[str] = [
        "===== Web Log Summary =====",
        f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Total Requests: {total_requests}",
        f"404 Errors: {errors_404}",
        "",
        "Top Requested URLs:"
    ]

    for url, count in top_urls:
        report_lines.append(f"  {url} - {count} hits")

    report_lines.append("")
    report_lines.append("Top IP Addresses:")
    for ip, count in top_ips:
        report_lines.append(f"  {ip} - {count} requests")

    report_lines.append("============================")

    report_text: str = "\n".join(report_lines)

    with open(output_file, "w") as f:
        f.write(report_text)

