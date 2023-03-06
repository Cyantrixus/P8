import os
import time
import auxiliary as aux
from roadnet import Roadnet
from processor import Processor

# Files
dataPath = os.path.abspath(r"./Data/taxi_log_2008_by_id")
outputPath = os.path.abspath(r"./Graphs")
files = os.listdir(dataPath)

# Create processor
print("CREATING PROCESSOR")
time_start = time.time()
processor = Processor()
map = Roadnet('CPH', "Copenhagen, Denmark", outputPath)
map.write()
time_process = time.time() - time_start
print(f"PROCESSOR READY: {time_process} SECONDS")

# Read CSV files
for file in files:
    processor.read(dataPath + "/" + file)
    break

# Print time log
done = time.time() - time_process - time_start
print(f"TIME TO READ: {done} SECONDS")
print(f"DATA SIZE: {len(processor.data)}")

# Load + lookup example
#print(f"LOADING {map.name} MAP")
#data = map.load()
#sample = data.head()
#row = map.lookup(sample, aux.idpred, 0)
#print(row)