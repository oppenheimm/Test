import math

a = int(input(""))
b = int(input(""))
c = int(input(""))

s = (a + b + c) / 2

y = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(y)
