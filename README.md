# Linux-System-Monitor
# Linux System Monitoring Tool

A Python-based monitoring system that tracks system resource usage and generates alerts.

## Features

- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Configurable thresholds
- Alert logging
- Service health monitoring
- Automated execution using cron

## Technologies Used

- Python
- psutil
- Linux
- cron

## Project Architecture

System Metrics → Threshold Detection → Alert Generation → Log Storage

## How to Run

Install dependencies:

pip3 install -r requirements.txt

Run the script:

python3 monitor.py

## Example Output

CPU Usage: 25%
Memory Usage: 40%
Disk Usage: 55%

ALERT: CPU usage high
