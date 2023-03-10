import os
import osmnx as osm
import numpy as np
import pandas as pd
import geopandas as gpd
import json

from pytrack.graph import graph, distance
from pytrack.analytics import visualization
from pytrack.matching import candidate, mpmatching_utils, mpmatching


class Roadnet:
    # Initialize a new instance by getting the graph from OSM
    def __init__(self, name, place, path):
        self.name  = name
        self.path  = path
        filename = self.path + "/" + self.name + ".json"
        if os.path.isfile(filename):
            with open(self.path + "/" + self.name + ".json", "r", encoding="utf8") as file:
                self.json = json.load(file)
                self.graph = graph.create_graph(self.json)
        else:
            # # Create BBOX
            location = osm.geocoder.geocode(place)
            north, south, east, west = osm.utils_geo.bbox_from_point(location, 10000)
            self.json = graph.download.osm_download(distance.enlarge_bbox(north, south, west, east, 500))
            self.graph = graph.create_graph(self.json)

    # Write the graph to disk as a graphml file if a file doesnt exist with that name
    def write(self):
        # Check file
        filename = self.path + "/" + self.name + ".json"
        if os.path.isfile(filename):
            print("NETWORK ALREADY SAVED")
            return
        
        # Check path
        if not os.path.isdir(self.path):
            os.makedirs(self.path)
        
        #Save Graph
        print("SAVING NETWORK")
        with open(self.path + "/" + self.name + ".json", "w", encoding="utf8") as file:
            json.dump(self.json, file, ensure_ascii=False, indent=2)

    # Load a GraphML file and return the object
    def load(self):
        filename = self.path + "/" + self.name + ".graphml"
        if not os.path.isfile(filename):
            print("NETWORK DOES NOT EXIST")
            return
        return osm.io.load_graphml(filename)
    
    def match(self, route):
        G_interp, candidates = candidate.get_candidates(self.graph, route)
        trellis = mpmatching_utils.create_trellis(candidates)
        path_prob, predecessor = mpmatching.viterbi_search(G_interp, trellis, "start", "target")
        return mpmatching_utils.create_matched_path(self.graph, trellis, predecessor)(trellis, predecessor, "start", "target")

    def match_visualize(self, route):
        pass
        #loc = (np.mean(latitudes), np.mean(longitudes))
        #maps = visualization.Map(location=loc, zoom_start=15)
        #maps.add_graph(G, plot_nodes=True)
        #G_interp, candidates = candidate.get_candidates(G, points, interp_dist=5, closest=True, radius=100)
        #trellis = mpmatching_utils.create_trellis(candidates)
        #path_prob, predecessor = mpmatching.viterbi_search(G_interp, trellis, "start", "target")

        #maps.draw_path(G_interp, trellis, predecessor, "MatchedMap")
        #maps.save(outputPath + "/" + "MatchedMap.html", close_file=True)

    # Lookup an item in the map with the the partial function f(item)
    # Note: Only finds the first occurence of the item (the keys should be unique most of the time)
    # def lookup(self, gpkg, f, item):
    #     pred = partial(f, item)
    #     for row in gpkg.itertuples():
    #         if pred(row):
    #             return row
    #     return None