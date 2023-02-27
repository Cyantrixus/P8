import os
import time
from processor import Processor

path = os.path.abspath(r"./Data/taxi_log_2008_by_id")
files = os.listdir(path)

t0 = time.time()
p = Processor()

for file in files:
    p.read(path + "/" + file)

done = time.time() - t0
print(f"TIME TO READ: {done} SECONDS")
print(f"DATA SIZE: {len(p.data)}")