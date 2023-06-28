import datetime
import time
import os

# La solucion del profesor
while True:
    os.system("cls")
    now = datetime.datetime.now()
    print(f"{now.hour:02d}:{now.minute:02d}:{now.second:02d}")
    time.sleep(1)

"""
Mi solucion:

start_time = datetime.datetime.now()

hours = start_time.hour
minutes = start_time.minute
seconds = start_time.second

while True:
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    seconds += 1

    if seconds > 59:
        seconds = 0
        minutes += 1
    
    if minutes > 59:
        seconds = 0
        minutes = 0
        hours += 1
    
    if hours > 23:
        hours = 0
        minutes = 0
        seconds = 0

    time.sleep(1)
    os.system("cls")
"""
