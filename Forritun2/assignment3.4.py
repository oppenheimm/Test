x = int(input())

print(x)

while x != 1:
    if x % 2 == 0:
        x = int(x / 2)
        print(x)
    else:
        x = int((x * 3) + 1)
        print(x)
