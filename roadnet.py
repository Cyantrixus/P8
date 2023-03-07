import os
import osmnx as ox
import numpy as np
import pandas as pd
import geopandas as gpd


class Roadnet:
    # Initialize a new instance by getting the graph from OSM
    def __init__(self, name, place, path):
        self.name  = name
        self.path  = path
        filename = self.path + "/" + self.name + ".graphml"
        if os.path.isfile(filename):
            self.graph = ox.io.load_graphml(filename)
        else:
            self.graph = ox.graph_from_place(place, network_type='drive')
    
    # Write the graph to disk as a gpkg file if a file doesnt exist with that name
    def write(self):
        # Check file
        filename = self.path + "/" + self.name + ".graphml"
        if os.path.isfile(filename):
            print("NETWORK ALREADY SAVED")
            return
        
        # Check path
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        
        #Save Graph
        print("SAVING NETWORK")
        ox.io.save_graphml(self.graph, filename, encoding="utf-8")

    # Load a GraphML file and return the object
    def load(self):
        filename = self.path + "/" + self.name + ".graphml"
        if not os.path.isfile(filename):
            print("NETWORK DOES NOT EXIST")
            return
        return ox.io.load_graphml(filename)
    
    # Lookup an item in the map with the the partial function f(item)
    # Note: Only finds the first occurence of the item (the keys should be unique most of the time)
    # def lookup(self, gpkg, f, item):
    #     pred = partial(f, item)
    #     for row in gpkg.itertuples():
    #         if pred(row):
    #             return row
    #     return None