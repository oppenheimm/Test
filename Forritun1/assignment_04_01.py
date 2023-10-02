# Author: tomas bragi
# Date: 2/25/2023
# Project: skilaverk 4 d 1
# Acknowledgements: tekið úr fyrirlestrartíma 

def get_input():
    numbers = []
    
    while True:
        current_input = input('Value: ')
        if current_input == 'done':
            break
        try:
            current_number = float(current_input)
            numbers.append(current_number)
        except ValueError:
            print('Invalid input')
            continue

    return numbers

numbers = get_input()

pivot = float(input('Pivot: '))

numbers_smaller = []
numbers_larger = []
for i in numbers:
    if i >= pivot:
        numbers_larger.append(i)
    elif i < pivot:
        numbers_smaller.append(i)

numbers_larger_sorted = sorted(numbers_larger)
numbers_smaller_sorted = sorted(numbers_smaller)
numbers_smaller_sorted.reverse()

output_smaller = []
output_larger = []
for num in numbers:
    if num in numbers_smaller_sorted:
        output_smaller.append(str(num))
    elif num in numbers_larger_sorted:
        output_larger.append(str(num))

print(' '.join(output_smaller))
print(' '.join(output_larger))