import psutil
import logging
import os
import time

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Setup logging
logging.basicConfig(
    filename='logs/system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 30
DISK_THRESHOLD = 10
PROCESS_COUNT_THRESHOLD = 300

# Colors for console alerts
RED = "\033[91m"
RESET = "\033[0m"

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU Usage: {usage}%')
        print(f"{RED}ALERT! High CPU Usage: {usage}%{RESET}")
        # Show top 3 CPU-consuming processes
        top_procs = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']),
                           key=lambda p: p.info['cpu_percent'], reverse=True)[:3]
        for proc in top_procs:
            logging.warning(f"Process {proc.info['name']} (PID {proc.info['pid']}): {proc.info['cpu_percent']}%")
            print(f"{RED}Process {proc.info['name']} (PID {proc.info['pid']}): {proc.info['cpu_percent']}%{RESET}")

def check_memory():
    mem = psutil.virtual_memory()
    usage = mem.percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory Usage: {usage}%')
        print(f"{RED}ALERT! High Memory Usage: {usage}%{RESET}")

def check_disk():
    disk = psutil.disk_usage('/')
    usage = disk.percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'High Disk Usage: {usage}%')
        print(f"{RED}ALERT! High Disk Usage: {usage}%{RESET}")

def check_processes():
    count = len(psutil.pids())
    if count > PROCESS_COUNT_THRESHOLD:
        logging.warning(f'High number of processes: {count}')
        print(f"{RED}ALERT! High number of processes: {count}{RESET}")

def main():
    while True:
        check_cpu()
        check_memory()
        check_disk()
        check_processes()
        time.sleep(5)  # Check every 5 seconds

if __name__ == '__main__':
    main()
