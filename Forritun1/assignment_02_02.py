# Author: Tomas Bragi
# Date: 1/18/2023 
# Project: Skilad 2 d.2
# Aknowledgements: fekk inblastur af koda a stackoverflow 
# aknowledgements: vann með tristan Elí

Value = int(input("Value: "))

Value_list=[]

while Value != 0:
    Value_list.append(Value)
    if Value < 0:
       break
    Value=int(input("Value: "))

    value_sum= sum(Value_list)
print("Total:",value_sum)