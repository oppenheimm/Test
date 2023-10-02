numbers = []

QUIT = "quit"


def dev():
    i = float(len(numbers))
    j = float(max(numbers))
    print((j - i) / i)


def rep():
    repeated_numbers = []
    for x in set(numbers):
        if numbers.count(x) > 1:
            repeated_numbers.append(x)
    return sorted(repeated_numbers, key=float)


def isNumber(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


inputval = input("Value: ")
while inputval != QUIT:
    if isNumber(inputval):
        numbers.append(inputval)
    else:
        print("Invalid input")

    inputval = input("Value: ")

print(", ".join(numbers))
dev()
rep()
repeated = rep()
if repeated:
    print("Repeated numbers in ascending order:", ", ".join(repeated))
else:
    print("No repeated numbers")
