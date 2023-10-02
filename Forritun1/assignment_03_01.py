# Author: <Tómas Bragi Þorvaldsson> 
# Date: <2.1.2023> 
# Project: <skilaverk 3 d 1> 
# aknowledgements: fekk hjalp fra Ívari

name = input("Name: ")

def format_name(name):
    first,last = name.split(", ")
    new=""
    new += last[0].upper()+". "
    new += first.capitalize()
    return new


print(format_name(name))