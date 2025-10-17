import random
from datetime import datetime, timedelta

log_file = "sample_logs/access.log"
num_entries = 500 


ips = ["192.168.1.10", "192.168.1.11", "10.0.0.2", "10.0.0.3", "127.0.0.1"]
methods = ["GET", "POST", "PUT", "DELETE"]
urls = ["/index.html", "/dashboard", "/api/data", "/login", "/contact", "/about", "/products"]
status_codes = [200, 200, 200, 404, 500, 403] 
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "curl/7.68.0",
    "PostmanRuntime/7.26.8"
]

with open(log_file, "w") as f:
    now = datetime.now()
    for _ in range(num_entries):
        ip = random.choice(ips)
        method = random.choice(methods)
        url = random.choice(urls)
        status = random.choice(status_codes)
        size = random.randint(100, 5000)
        agent = random.choice(user_agents)
        timestamp = (now - timedelta(seconds=random.randint(0, 86400))).strftime("%d/%b/%Y:%H:%M:%S +0000")
        log_line = f'{ip} - - [{timestamp}] "{method} {url} HTTP/1.1" {status} {size} "{agent}"\n'
        f.write(log_line)

print(f"Generated {num_entries} log entries in {log_file}")
