import os
import osmnx as osm
import numpy as np
import pandas as pd
import geopandas as gpd
from fmm import Network,NetworkGraph,STMATCH,STMATCHConfig


class Roadnet:
    # Initialize a new instance by getting the graph from OSM
    def __init__(self, name, place, path):
        self.name  = name
        self.path  = path
        filename = self.path + "/" + self.name
        if os.path.isfile(filename + ".shp"):
            print("NETWORK ALREADY SAVED")
        else:
            print("SAVING NETWORK")
            graph = osm.graph_from_place(place, network_type='drive')
            
            # Create files
            node_file = os.path.join(self.path, "nodes.shp")
            edge_file = os.path.join(self.path, "edges.shp")

            nodes, edges = osm.utils_graph.graph_to_gdfs(graph)
            nodes = osm.io._stringify_nonnumeric_cols(nodes)
            edges = osm.io._stringify_nonnumeric_cols(edges)

            edges["fid"] = np.arange(0, edges.shape[0], dtype='int')

            nodes.to_file(node_file, encoding='utf-8')
            edges.to_file(edge_file, encoding='utf-8')
    
    def match(self, points):
        # Load roadnet from path
        roadnet = Network(self.path + "/" + "edges.shp")
        print(f"Nodes: {roadnet.get_node_count()}, Edges: {roadnet.get_edge_count()}")

        # Configuration variables
        k = 4
        e = 0.5
        r = 0.4
        vmax = 30
        factor = 1.5

        # FMM Config
        config = STMATCHConfig(k, r, e, vmax, factor)
        graph = NetworkGraph(roadnet)
        model = STMATCH(roadnet, graph)

        # Construct wtk string
        pairs = [f"{lat} {long}" for (lat, long) in points]
        wtk = "LINESTRING("
        for xy in pairs:
            wtk = wtk + xy + ","
        wtk = wtk + ")"

        # Return match
        return model.match_wtk(wtk, config)

    # Lookup an item in the map with the the partial function f(item)
    # Note: Only finds the first occurence of the item (the keys should be unique most of the time)
    # def lookup(self, gpkg, f, item):
    #     pred = partial(f, item)
    #     for row in gpkg.itertuples():
    #         if pred(row):
    #             return row
    #     return None