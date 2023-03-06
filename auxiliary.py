# lambdas for looking up values in streetmap
#x type: Int
idpred = lambda x, y: y.Index == x

#x type: Int
osmpred = lambda x, y: y.osmid == x

#x type: int
ypred = lambda x, z: z.y == x

#x type: Int
xpred = lambda x, y: y.x == x

#x type: Int
streetpred = lambda x, y: y.street_count == x

#x type: String
roadpred = lambda x, y: y.highway == x

#x type: <POINT(x,y)>
geopred = lambda x, y: y.geometry == x