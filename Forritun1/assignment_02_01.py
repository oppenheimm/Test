# Author: Tomas Bragi
# Date: 1/18/2023 
# Project: Skilad 2 d.1
# Aknowledgements: hjalpadi Tristan eli med kodan

d1 = int(input("Input first dice: "))
d2 = int(input("Input second dice: "))
sum = d1+d2
if  d1 <1 or d1 >6 or d2 <1 or d2>6:
    print("Invalid input")
elif sum== 7 or sum== 11:
    print("Winner")
elif sum== 2 or sum== 3 or sum== 11:
    print("Loser")
else:
    print(sum)