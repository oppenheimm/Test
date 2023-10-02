# Author: <Tomas Bragi Thorvaldsson> 
# Date: <1/10/23> 
# Project: <skiladaemi 1, daemi 4>
import math

p1x=float(input("Point 1, x coordinate: " ))
p1y=float(input("Point 1, y coordinate: " ))
p2x=float(input("Point 2, x coordinate: " ))
p2y=float(input("Point 2, y coordinate: " ))


distxy= math.sqrt(((p1x - p2x)**2) + ((p1y - p2y)**2))

print("The distance between (",p1x,",",p1y,") and (",p2x,",",p2y,") is",distxy)