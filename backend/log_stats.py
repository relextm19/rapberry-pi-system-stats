import psutil
import subprocess
import re
import os
import csv
from time import sleep

PATH = 'temp/stats_log.csv'
HEADERS = ['CPU Usage', 'CPU Temp', 'Memory Usage', 'Disk Usage', 'Network Usage', 'Boot Time']

def get_CPU_temp():
    msg = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'\d+\.\d+', msg)   
        try:
            temp = float(m.group())
        except ValueError: 
            pass
    return temp

def get_memory_stats():
    return list(psutil.virtual_memory())[1:4] # Convert named tuple to list

def get_disk_stats():
    return list(psutil.disk_usage('/'))[1:4] # Convert named tuple to list

def get_network_stats():
    return list(psutil.net_io_counters())[1:4] # Convert named tuple to list

def get_system_stats():
    sys_stats = [
        psutil.cpu_percent(interval=1),
        get_CPU_temp(),
        get_memory_stats(),
        get_disk_stats(),
        get_network_stats(),
        psutil.boot_time(),
    ]
    return sys_stats

def write_to_file(writer):
    writer.writerow(get_system_stats())

def main():
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    FILE = open(PATH, 'a')
    writer = csv.writer(FILE)
    writer.writerow(HEADERS)

    while True: 
        write_to_file(writer)
        sleep(1)

if __name__ == "__main__":
    main()