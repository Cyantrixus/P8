import os
import time
from Beijing import Beijing
from Processor import Processor

# Files
dataPath = os.path.abspath(r"./Data/taxi_log_2008_by_id")
outputPath = os.path.abspath(r"./Output")
files = os.listdir(dataPath)

# Create processor
print("CREATING PROCESSOR")
time_start = time.time()
p = Processor()
print("SAVING BEIJING NETWORK")
beijing = Beijing('Beijing', outputPath)
beijing.write()
time_process = time.time() - time_start
print(f"PROCESSOR READY: {time_process} SECONDS")

# Read CSV files
for file in files:
    p.read(dataPath + "/" + file)
    break

# Print time log
done = time.time() - time_process - time_start
print(f"TIME TO READ: {done} SECONDS")
print(f"DATA SIZE: {len(p.data)}")