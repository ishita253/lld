import psutil

for proc in psutil.process_iter(['pid', 'name']):
    try:
        print(f"{proc.info['pid']}: {proc.info['name']}")
    except psutil.NoSuchProcess:
        pass

'''
linux version
import os

for pid in os.listdir('/proc'):
    if pid.isdigit():
        try:
            with open(f'/proc/{pid}/comm') as f:
                name = f.read().strip()
                print(f"{pid}: {name}")
        except:
            pass  # Process may have exited or permission denied

'''