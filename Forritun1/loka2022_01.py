QUIT = "done"
numbers = []


def isNumber(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


class Number:
    def __init__(self, value):
        self.value = value
        self.float_value = float(value)


def print_small():
    small_numbers = []
    for number in numbers:
        if number.float_value < pivot:
            small_numbers.append(number.value)
    print(" ".join(small_numbers))


def print_large():
    large_numbers = []
    for number in numbers:
        if number.float_value > pivot:
            large_numbers.append(number.value)
    print(" ".join(large_numbers))


inputval = input("Value: ")
while inputval != QUIT:
    if isNumber(inputval):
        numbers.append(Number(inputval))
    else:
        print("Invalid input")

    inputval = input("Value: ")

pivot = float(input("Pivot: "))

print_small()
print_large()
