import re
import logging

LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+'        
    r'\[(?P<time>[^\]]+)\]\s+'                        
    r'"(?P<method>[A-Z]+)\s(?P<url>[^\s]+)\s[^"]+"\s' 
    r'(?P<status>\d{3})\s+'                           
    r'(?P<size>\d+|-)'                               
)

def parse_log_line(line):
    match = LOG_PATTERN.search(line)
    if match:
        data = match.groupdict()
        data['status'] = int(data['status'])
        data['size'] = int(data['size']) if data['size'].isdigit() else 0
        return data
    else:
        logging.warning(f"Malformed log line skipped: {line.strip()}")
    return None

