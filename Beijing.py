import os
import numpy as np
import osmnx as ox

class Beijing:
    def __init__(self, name, path):
        self.name  = name
        self.path  = path
        self.graph = ox.graph_from_place("Beijing, China", network_type='drive')

    def write(self):
        # Create directory and save file if it doesnt exist
        if not self.path == "" and not os.path.exists(self.path):
            os.makedirs(self.path)
            ox.io.save_graph_geopackage(self.graph, self.path + "/" + self.name)
        else:
            print("ROAD NETWORK ALREADY SAVED")