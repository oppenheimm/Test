# Author: <Tomas Bragi Thorvaldsson> 
# Date: <1/10/23> 
# Project: <skiladaemi 1, daemi 3>

x = int(input("How many seconds? "))
h = int(x/3600)
m = int((x-(h*3600))/60)
s = int((x-(h*3600)-(m*60)))
print("Hours:",h)
print("Minutes:",m)
print("Seconds:",s)