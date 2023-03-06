import os
import osmnx as ox
import numpy as np
import pandas as pd
import geopandas as gpd
from functools import partial

class Roadnet:
    # Initialize a new instance by getting the graph from OSM
    def __init__(self, name, place, path):
        self.name  = name
        self.path  = path
        self.graph = ox.graph_from_place(place, network_type='drive')
    
    # Write the graph to disk as a gpkg file if a file doesnt exist with that name
    def write(self):
        # Check file
        filename = self.path + "/" + self.name + ".gpkg"
        if os.path.isfile(filename):
            print("NETWORK ALREADY SAVED")
            return
        
        # Check path
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        
        #Save Graph
        print("SAVING NETWORK")
        ox.io.save_graph_geopackage(self.graph, filename, encoding="utf-8")

    # Load a gpkg file and return the object
    def load(self):
        filename = self.path + "/" + self.name + ".gpkg"
        if not os.path.isfile(filename):
            print("NETWORK DOES NOT EXIST")
            return
        return gpd.read_file(filename)
    
    # Lookup an item in the map with the the partial function f(item)
    # Note: Only finds the first occurence of the item (the keys should be unique most of the time)
    def lookup(self, gpkg, f, item):
        pred = partial(f, item)
        for row in gpkg.itertuples():
            if pred(row):
                return row
        return None
