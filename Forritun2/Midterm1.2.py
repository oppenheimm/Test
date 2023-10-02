count = int(input())

value = 0

for i in range(count + 1):
    n = 1 / (2**i)
    value = value + n
    if value - 1 != 0:
        print(value - 1)
