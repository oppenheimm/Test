def convert_to_float(number_as_str):
    try:
        result = float(number_as_str)
        return result
    except ValueError:
        print('Invalid input')
        return None

def update_duplicates(value, measurements, repeated_values):
    if value in measurements and value not in repeated_values:
        repeated_values.append(value)

def get_measurements():
    measurements = []
    repeated_values = []   # part-b

    user_input = input('Measurement: ')
    while user_input != 'quit':
        value = convert_to_float(user_input)

        if value is not None:
            update_duplicates(value, measurements, repeated_values) # part-b
            measurements.append(value)

        user_input = input('Measurement: ')

    return measurements, repeated_values

def get_largest_deviation(measurements):
    average = sum(measurements)/len(measurements)
    largest_deviation = 0
    for m in measurements:
        if abs((average - m) / average) > largest_deviation:
            largest_deviation = abs((average - m)/average)
    return average, round(100*largest_deviation)


measurements, repeated_values = get_measurements()
average, largest_deviation = get_largest_deviation(measurements)

print('Measurements:', ', '.join([str(m) for m in measurements]))
print(f'Largest deviation: {largest_deviation}%')

if len(repeated_values) > 0:   # part-b
    print('Repeated values:', ', '.join([str(x) for x in sorted(repeated_values)]))


    