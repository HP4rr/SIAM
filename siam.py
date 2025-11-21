#1/usr/bin/env python3
"""
SIAM - System Integrity and Anomaly Monitor
v0.1 - Initial live process list
Author: [Carson Hale]
Date: 2025-11-20
"""

import psutil
import os
import time

os.system('clear')

while True:
    print ('SIAM v0.1 - Process Monitor. (0.2s refresh)')
    print ('Press Cntrl+C to stop.\n')
    
    for process in psutil.process_iter():
        processes = f"PID: {process.pid} | Name: {process.name()}"
        print (processes)
        time.sleep(.2)


     
        
        
        
        
        
        
    

