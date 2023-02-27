import os
import numpy as np
import osmnx as ox

class Beijing:
    def __init__(self, name, path):
        self.name  = name
        self.path  = path
        self.graph = ox.graph_from_place("Beijing, China", network_type='drive')

    def write(self):
        # Create directory if it doesnt exist
        if not self.path == "" and not os.path.exists(self.path):
            os.makedirs(self.path)
    
        # Write shape files
        nodefile = os.path.join(self.path, "nodes.shp")
        edgefile = os.path.join(self.path, "edges.shp")

        # Convert undirected graph to gdfs and stringify non-numeric columns
        nodes, edges = ox.utils_graph.graph_to_gdfs(self.graph)
        nodes = ox.io._stringify_nonnumeric_cols(nodes)
        edges = ox.io._stringify_nonnumeric_cols(edges)

        # We need an unique ID for each element in the given vector
        ids = lambda x: np.arange(1, len(x)+1, 1)

        #Assign ids
        edges["key"] = ids(edges)
        nodes["node"] = ids(nodes)