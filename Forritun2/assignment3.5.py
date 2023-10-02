number = int(input())
contains_seven = False

while number != 0:
    digit = number % 10
    if digit == 7:
        contains_seven = True
        break
    number = number // 10

if contains_seven:
    print("The number contains 7.")
else:
    print("The number does not contain 7.")
