import psutil
import logging
import json
import subprocess
import os
from datetime import datetime

# -----------------------------
# Logging Configuration
# -----------------------------
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "system_monitor.log")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -----------------------------
# Load Configuration
# -----------------------------
try:
    with open("config.json") as f:
        config = json.load(f)
except Exception as e:
    print("Error loading config file:", e)
    exit(1)

CPU_THRESHOLD = config.get("cpu_threshold", 80)
MEMORY_THRESHOLD = config.get("memory_threshold", 80)
DISK_THRESHOLD = config.get("disk_threshold", 90)
SERVICES = config.get("services", ["httpd"])

# -----------------------------
# System Metrics Functions
# -----------------------------
def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

    if cpu > CPU_THRESHOLD:
        alert = f"ALERT: CPU usage high ({cpu}%)"
        print(alert)
        logging.warning(alert)


def check_memory():
    memory = psutil.virtual_memory()
    mem_usage = memory.percent

    print(f"Memory Usage: {mem_usage}%")

    if mem_usage > MEMORY_THRESHOLD:
        alert = f"ALERT: Memory usage high ({mem_usage}%)"
        print(alert)
        logging.warning(alert)


def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent

    print(f"Disk Usage: {disk_usage}%")

    if disk_usage > DISK_THRESHOLD:
        alert = f"ALERT: Disk usage high ({disk_usage}%)"
        print(alert)
        logging.warning(alert)


# -----------------------------
# Service Monitoring
# -----------------------------
def check_services():
    for service in SERVICES:
        try:
            status = subprocess.run(
                ["systemctl", "is-active", service],
                capture_output=True,
                text=True
            )

            if status.stdout.strip() != "active":
                alert = f"ALERT: Service {service} is NOT running"
                print(alert)
                logging.error(alert)
            else:
                print(f"Service {service}: running")

        except Exception as e:
            logging.error(f"Error checking service {service}: {e}")


# -----------------------------
# Main Function
# -----------------------------
def main():

    print("\n========== SYSTEM MONITOR ==========")
    print(f"Time: {datetime.now()}")
    print("====================================\n")

    check_cpu()
    check_memory()
    check_disk()
    check_services()

    print("\nMonitoring complete.\n")


if __name__ == "__main__":
    main()
