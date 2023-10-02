# Author: Tomas Bragi
# Date: 1/18/2023 
# Project: Skilad 2 d.4
# aknowledgements: vann með tristan Elí


Value = int(input("Value: "))

Value_list=[]

while Value != 0:
    Value_list.append(Value)
    if Value < 0:
       break
    Value=int(input("Value: "))

length = len(Value_list)
Value_list.sort()
print("Largest:",Value_list[length-1])
print("Second largest:",Value_list[length-2])

