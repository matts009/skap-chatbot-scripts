import os

script = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'retrieve_schedule.py')

print script

#execfile(script)

os.spawnl(os.P_WAIT, 'C:\Python27\python.exe', 'python.exe', script)