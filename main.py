import os
import time
import numpy as np
import osmnx as osm
from roadnet import Roadnet
from processor import Processor

from pytrack.graph import graph, distance
from pytrack.analytics import visualization
from pytrack.matching import candidate, mpmatching_utils, mpmatching

# Files
dataPath = os.path.abspath(r"./Data/taxi_log_2008_by_id")
outputPath = os.path.abspath(r"./Graphs")
files = os.listdir(dataPath)

# Create processor
print("CREATING PROCESSOR")
time_start = time.time()

processor = Processor()
map = Roadnet('BJ', "Beijing", outputPath)
map.write()

# Processor ready
time_process = time.time() - time_start
print(f"PROCESSOR READY: {time_process} SECONDS")

# Read CSV files
for file in files:
    processor.read(dataPath + "/" + file)
    break
    # print(processor.data[0]["long"])

# Print read log
done = time.time() - time_process - time_start
print(f"TIME TO READ: {done} SECONDS")
print(f"DATA SIZE: {len(processor.data)}")

# Map matching
processor.write_points()
path = map.match(processor.routes[0])
print(path)

#loc = (np.mean(latitudes), np.mean(longitudes))
#maps = visualization.Map(location=loc, zoom_start=15)
#maps.add_graph(G, plot_nodes=True)

#G_interp, candidates = candidate.get_candidates(G, points, interp_dist=5, closest=True, radius=100)
#trellis = mpmatching_utils.create_trellis(candidates)
#path_prob, predecessor = mpmatching.viterbi_search(G_interp, trellis, "start", "target")

#maps.draw_path(G_interp, trellis, predecessor, "MatchedMap")
#maps.save(outputPath + "/" + "MatchedMap.html", close_file=True)

# Load + lookup example
#print(f"LOADING {map.name} MAP")
#data = map.load()
#sample = data.head()
#row = map.lookup(sample, aux.idpred, 0)
#print(row)