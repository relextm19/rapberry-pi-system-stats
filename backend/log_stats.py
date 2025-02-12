import psutil
import subprocess
import re
from time import sleep

PATH = 'temp/stats_log.log'

def get_CPU_temp():
    msg = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)   
        try:
            temp = float(m.group())
        except ValueError: 
            pass
    return temp

def get_memory_stats():
    stats = list(psutil.virtual_memory()._asdict().values()) #turn bytes into a dict then get values and turn it to a list
    return stats[:4]

def get_disk_stats():
    return list(psutil.disk_usage('/')._asdict().values()) #turn bytes into a dict then get values and turn it to a list

def get_network_stats():
    stats = list(psutil.net_io_counters()._asdict().values()) #turn bytes into a dict then get values and turn it to a list
    return stats[:4]

def get_system_stats():
    sys_stats = {
        'cpu_percent': psutil.cpu_percent(interval=1),
        'cpu_temperature': get_CPU_temp(),
        'memory_stats': get_memory_stats(),
        'disk_stats': get_disk_stats(),
        'network_io': get_network_stats(),
        'uptime': psutil.boot_time(),
    }
    return sys_stats

def write_to_file():
    stats = get_system_stats()
    with open(PATH, 'a') as log_file:
        buf = '{'
        for value in stats.values():
            buf += str(value) + ','
        buf = buf[:-1] #remove last comma
        buf += '},'
        log_file.write(buf)

def main():
    while True:
        write_to_file()
        sleep(1)

main()