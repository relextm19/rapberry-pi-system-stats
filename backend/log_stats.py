import psutil
import subprocess
import re
import os
from time import sleep

PATH = 'temp/stats_log.log'

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
    stats = list(psutil.virtual_memory()) # Convert named tuple to list
    return stats[:4]

def get_disk_stats():
    return list(psutil.disk_usage('/')) # Convert named tuple to list

def get_network_stats():
    stats = list(psutil.net_io_counters()) # Convert named tuple to list
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
        buf = ''
        for stat in stats.values():
            print(stat)
            try: #itterate through array or add a number
                for data in stat:
                    buf += str(data) + ','
            except TypeError:
                buf += str(stat) + ','
        
        log_file.write(buf)

def main():
    os.makedirs(os.path.dirname(PATH), exist_ok=True)

    while True:
        write_to_file()
        sleep(1)

if __name__ == "__main__":
    main()