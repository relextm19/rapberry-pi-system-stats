import psutil
import subprocess
import re
import os
import csv
from time import time, sleep
import math

PATH = 'temp/stats_log.csv'
HEADERS = ['CPU Stats', 'Memory Stats', 'Network Stats', 'Up Time']

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
    #[available_memory, percentage_used, used_memory]
    stats = list(psutil.virtual_memory())[1:4] # Convert named tuple to list
    stats[0] = round(stats[0] / (1024 ** 3), 2)
    stats[2] = round(stats[2] / (1024 ** 3), 2)

    return stats

def get_network_stats():
    #[bytes_sent, bytes_received, packets_sent, packets_received]
    return list(psutil.net_io_counters())[0:4] # Convert named tuple to list

def get_CPU_stats():
    return [psutil.cpu_percent(interval=1), get_CPU_temp()]  #this sleeps for 1 second which is fine

def get_system_stats():
    return [
        get_CPU_stats(),
        get_memory_stats(),
        get_network_stats(),
        f'{(time() - psutil.boot_time()):.2f}',
    ]

def write_to_file(writer, file):
    writer.writerow(get_system_stats())
    file.flush()

def main():
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    if os.path.exists(PATH):
        os.remove(PATH)
    FILE = open(PATH, 'a')
    writer = csv.writer(FILE)
    writer.writerow(HEADERS)

    while True: #the loop is slept for 1 second due to the blocking cpu stats call but its fine
        write_to_file(writer, FILE) 

if __name__ == "__main__":
    main()