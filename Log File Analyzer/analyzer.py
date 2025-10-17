from collections import Counter

def analyze_logs(parsed_logs):
    total_requests = len(parsed_logs)
    status_counter = Counter(entry['status'] for entry in parsed_logs)
    url_counter = Counter(entry['url'] for entry in parsed_logs)
    ip_counter = Counter(entry['ip'] for entry in parsed_logs)

    summary = {
        "total_requests": total_requests,
        "404_errors": status_counter.get('404', 0),
        "top_urls": url_counter.most_common(5),
        "top_ips": ip_counter.most_common(5),
    }

    return summary

