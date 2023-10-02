# Author: <Tómas Bragi Þorvaldsson> 
# Date: <12.3.2023> 
# Project: <skilaverk 5 d 1> 



cancel = False
a= []
name1 = input("Student name: ")

while (True):
    g1 = float(input("Input grade number 1: "))
    g2 = float(input("Input grade number 2: "))
    g3 = float(input("Input grade number 3: "))

    a.append(g1)
    a.append(g2)
    a.append(g3)
    break
avga = float(sum(a)/len(a))

b= []
name2 = input("Student name: ")

while (True):
    g1 = float(input("Input grade number 1: "))
    g2 = float(input("Input grade number 2: "))
    g3 = float(input("Input grade number 3: "))

    b.append(g1)
    b.append(g2)
    b.append(g3)
    break
avgb = float(sum(b)/len(b))

c= []
name3 = input("Student name: ")

while (True):
    g1 = float(input("Input grade number 1: "))
    g2 = float(input("Input grade number 2: "))
    g3 = float(input("Input grade number 3: "))

    c.append(g1)
    c.append(g2)
    c.append(g3)
    break
avgc = float(sum(c)/len(c))

d= []
name4 = input("Student name: ")

while (True):
    g1 = float(input("Input grade number 1: "))
    g2 = float(input("Input grade number 2: "))
    g3 = float(input("Input grade number 3: "))

    d.append(g1)
    d.append(g2)
    d.append(g3)
    break
avgd = float(sum(d)/len(d))

x =[]
x.append(avga)
x.append(avgb)
x.append(avgc)
x.append(avgd)

print("Student list: ")
data = {name1: a, name2: b, name3: c, name4: d}
for name, value in sorted(data.items()):
    print(name + ": " + str(value))


print("Student with highest average grade:")
if max(x) == avga:
    print(name1, "has an average grade of {:.2f}".format(avga))
elif max(x) == avgb:
    print(name2, "has an average grade of {:.2f}".format(avgb))
elif max(x) == avgc:
    print(name3, "has an average grade of {:.2f}".format(avgc))
else:
    print(name4, "has an average grade of {:.2f}".format(avgd))