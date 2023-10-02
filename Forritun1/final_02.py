# Author: <Tomas bragi thorvaldsson>
# Date: <21/4/2023>
# Project: <final_02>


QUIT = "quit"
numbers = []


def isNumber(x):
    # docstring: this function checks if input is an integral
    try:
        int(x)
        return True
    except ValueError:
        return False


def palindrome():
    # this function mirrors the list
    size = len(numbers)
    mirrored = [[0] * size for _ in range(size)]
    for i in range(size):
        mirrored[i] = numbers[size - i - 1]
    return mirrored


inputval = input(" ")
while inputval != QUIT:
    if isNumber(inputval):
        numbers.append(inputval)
    else:
        print("Invalid input")

    inputval = input(" ")


if palindrome() == numbers:
    print("palindrome")

for num in numbers:
    x = 1
    while num - x == num + x:
        x = x + 1
