# Author: <Tomas Bragi Thorvaldsson> 
# Date: <1/10/23> 
# Project: <skiladaemi 1, daemi 2>

x = float(input("Write a 4 digit number: "))
z = int(x/1000)
y = float(((x/1000)-z)*(100))
print("The middle two digits are",int(y))