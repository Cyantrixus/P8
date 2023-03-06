import pandas as p


class Processor:
    headers = ["id", "time", "long", "lat"]
   # Start as empty
    def __init__(self):
        self.data = []
    
    # Read a csv file and store the data
    def read(self, path):
        df = p.read_csv(path, delimiter=',', names=self.headers)
        self.data.append(df)

#       csv = np.recfromcsv(path, delimiter=',', encoding="utf-8")
   
        