# log_parser.py

import re
import logging

# Corrected Apache/Nginx Common Log Format Regex
LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+'         # IP and two hyphens
    r'\[(?P<time>[^\]]+)\]\s+'                        # Timestamp
    r'"(?P<method>[A-Z]+)\s(?P<url>[^\s]+)\s[^"]+"\s' # HTTP Method + URL
    r'(?P<status>\d{3})\s+'                           # Status code
    r'(?P<size>\d+|-)'                                # Response size
)

def parse_log_line(line):
    """Parses a single line and returns a dict of extracted values."""
    match = LOG_PATTERN.search(line)
    if match:
        data = match.groupdict()
        # Convert types
        data['status'] = int(data['status'])
        data['size'] = int(data['size']) if data['size'].isdigit() else 0
        return data
    else:
        logging.warning(f"Malformed log line skipped: {line.strip()}")
    return None
