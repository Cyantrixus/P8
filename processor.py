import pandas as p
import geopandas as gp

class Processor:
   # Start as empty
    def __init__(self):
        self.data = []
        self.routes = []
    
    # Read a csv file and store the data as Pandas data frames
    def read(self, path):
        headers = ["id", "time", "long", "lat"]
        df = p.read_csv(path, delimiter=',', names=headers)
        self.data.append(df)

    # Create a vector of coordinates for each data point
    def write_points(self):
        for taxi in self.data:
            geodata = gp.GeoDataFrame(taxi, geometry=gp.points_from_xy(taxi.long, taxi.lat))
            latitude = geodata["lat"].to_list()
            longitude = geodata["long"].to_list()
            points = [(lat, long) for lat, long in zip(latitude, longitude)]
            self.routes.append(points)

    # Return a vector og latititude coordinates from a vector of points
    def write_latitude(self, points):
        return [lat for (lat, _) in points]
    
    # Return a vector og latititude coordinates from a vector of points
    def write_longitude(self, points):
        return [long for (_, long) in points]