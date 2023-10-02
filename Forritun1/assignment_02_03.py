# Author: Tomas Bragi
# Date: 1/18/2023 
# Project: Skilad 2 d.3
# aknowledgements: vann með tristan Elí

x1 = int(input("First number: "))
x2 = int(input("Second number: "))
x3 = int(input("Third number: "))

if x1 <= x2 and x1 >= x3 or x1 >= x2 and x1 <= x3:
    print("The middle number is:",x1)
elif x2 <= x1 and x2 >= x3 or x2 >= x1 and x2 <= x3:
    print("The middle number is:",x2)
else:
    print("The middle number is:",x3)