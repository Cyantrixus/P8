import numpy as np
#from pynapl import APL


class Processor:
    def __init__(self):
        #self.apl = APL.APL()
        self.data = []
    
    def read(self, path):
        # Numpy attempt
        csv = np.recfromcsv(path, delimiter=',', encoding="utf-8")
        self.data.append(csv)