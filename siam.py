
"""
SIAM - System Integrity and Anomaly Monitor
v0.2 - CPU, memory, and disk usage stats
Author: [Carson Hale]
Date: 2025-12-18
"""

import psutil
from psutil._common import bytes2human


# CPU Usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage} %")

# Memory Usage
memory_usage = psutil.virtual_memory()
print (f"Memory Usage: {memory_usage.percent}%")

# Disk Usage
disk_usage = psutil.disk_usage('/')
total_storage = disk_usage.total / (1024 ** 3)
free_storage = disk_usage.free / (1024 ** 3)
used_storage = disk_usage.used / (1024 ** 3)

print (f"Total storage: {total_storage:.2f} GB")
print (f"Free storage: {free_storage:.2f} GB")
print (f"Storage used: {used_storage:.2f} GB")



'''
while True:
    print ("SIAM v0.1 - Process Monitor")
    print ('Press Cntrl+C to stop.\n')
    for process in psutil.process_iter():
        processes = f"PID: {process.pid} | Name: {process.name()}"
        print (processes)
        time.sleep(.2)
'''
