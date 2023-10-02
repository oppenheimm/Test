# Author: Tomas bragi
# Date: 2/25/2023
# Project: Skilaverk 4 d 2
# Acknowledgements: byggt eitthvað á fyrirlestrardæmi í viku 7, stackoverflow kom líka til með að hjálpa


def sum_input_numbers(user_input):
    numbers = user_input.split()
    total = 0
    for number in numbers:
        total += int(number)
    return total

def get_inputs():
    inputs = []
    while True:
        user_input = input("Payments: ")
        if user_input.lower() == 'quit':
            break
        else:
            inputs.append(user_input)
    return inputs

def check_income_growing(inputs):
    income_growing = True
    for i in range(1, len(inputs)):
        if inputs[i] < inputs[i-1]:
            income_growing = False
            break
    return income_growing

inputs = get_inputs()

if len(inputs) > 0:
    previous_sum = None
    income_growing = True
    for user_input in inputs:
        result = sum_input_numbers(user_input)
        if previous_sum is not None and result < previous_sum:
            income_growing = False
        print(result)
        previous_sum = result
    if income_growing or all(x == inputs[0] for x in inputs):
        print("The income is growing.")
else:
    print("No inputs were provided.")
