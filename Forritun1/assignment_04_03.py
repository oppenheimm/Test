# Author: Tomas bragi
# Date: 2/26/2023
# Project: skilaverk 4 dæmi 4
# Acknowledgements: stackoverflow geeksforgeeks

def get_inputs():
    inputs = []
    while True:
        user_input = input("Measurement: ")
        if user_input.strip().lower() == 'quit':
            break
        if '.' in user_input and user_input.count('.') > 1:
            print("Invalid input")
            continue
        if all(c.isdigit() or c == '.' or c == '-' for c in user_input):
            inputs.append(float(user_input))
        else:
            print("Invalid input")
    return inputs

def get_repeated_values(inputs):
    repeated_values = set()
    unique_values = set()
    for value in inputs:
        if value in unique_values:
            repeated_values.add(value)
        else:
            unique_values.add(value)
    return repeated_values

def calculate_max_deviation_percent(inputs):
    n = len(inputs)
    mean = sum(inputs) / n
    max_deviation = max(abs(x - mean) for x in inputs)
    return round(abs(max_deviation / mean) * 100)

inputs = get_inputs()

if inputs:
    print("Measurements:", ', '.join(str(i) for i in inputs))
    print("Largest deviation: {}%".format(calculate_max_deviation_percent(inputs)))
    repeated_values = get_repeated_values(inputs)
    if repeated_values:
        print("Repeated values: {}".format(', '.join(str(i) for i in sorted(repeated_values))))
else:
    print("No inputs were provided.")
