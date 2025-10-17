A Python script to continuously monitor system health metrics and alert when thresholds are exceeded.

Features

- Monitor CPU usage, memory usage, disk usage, and number of running processes.
- Log alerts to a file and print them to the console with highlighting.
- Display top 3 CPU-consuming processes when CPU usage is high.
- Configurable thresholds for each metric.

Installation

Clone the repository:

git clone https://github.com/Matt-0013/python_scripts
cd system_health_monitor

(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Configuration

Thresholds can be adjusted directly in system_health_monitor.py:

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 30
DISK_THRESHOLD = 10
PROCESS_COUNT_THRESHOLD = 300

Logs are stored in logs/system_health.log.

Usage

Run the monitor:

python system_health_monitor.py

The script runs in an infinite loop, checking system health every 5 seconds.

Output

Console: Alerts highlighted in red when thresholds are exceeded.

Log file: Detailed logs stored in logs/system_health.log.