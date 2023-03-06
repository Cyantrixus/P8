import pandas as p
import geopandas as gp

class Processor:
   # Start as empty
    def __init__(self):
        self.data = []
        self.routes = []
    
    # Read a csv file and store the data
    def read(self, path):
        headers = ["id", "time", "long", "lat"]
        df = p.read_csv(path, delimiter=',', names=headers)
        self.data.append(df)

    def write_points(self):
        for taxi in self.data:
            geodata = gp.GeoDataFrame(taxi, geometry=gp.points_from_xy(taxi.long, taxi.lat))
            route = []
            for row in geodata.itertuples():
                tuple = (row.lat, row.long) # PyTrack docs har (lang, long) som punkter
                route.append(tuple)
            self.routes.append(route)