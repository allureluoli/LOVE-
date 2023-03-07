import datetime
import os
import time
from multiprocessing import Process




now = datetime.datetime.now()
time = now.strftime("%Y-%m-%d %H:%M:%S")
TMD=time.split(' ')[1].split(':')
H=int(TMD[0])*3600
M=int(TMD[0])*60
S=int(TMD[0])
TIMEONE= H+M+S

print(TMD)