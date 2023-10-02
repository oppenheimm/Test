import math

x1_str = input()
y1_str = input()
x2_str = input()
y2_str = input()

x1 = int(x1_str)
y1 = int(y1_str)
x2 = int(x2_str)
y2 = int(y2_str)

x = ((x2 - x1)) ** 2
y = ((y2 - y1)) ** 2
z = math.sqrt(x + y)
print(z)
