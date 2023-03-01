import numpy as np

class Processor:
    # Start as empty
    def __init__(self):
        self.data = []
    
    # Read a csv file and store the data
    def read(self, path):
        csv = np.recfromcsv(path, delimiter=',', encoding="utf-8")
        self.data.append(csv)
        