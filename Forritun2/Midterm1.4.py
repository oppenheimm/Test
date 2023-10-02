item = int(input())
paid = int(input())

change = paid - item

while change - 20 >= 0:
    print("20")
    change = change - 20

while change - 10 >= 0:
    print("10")
    change = change - 10

while change - 5 >= 0:
    print("5")
    change = change - 5

while change - 2 >= 0:
    print("2")
    change = change - 2

while change - 1 >= 0:
    print("1")
    change = change - 1
