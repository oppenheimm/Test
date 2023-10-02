import statistics


# this function reads the numbers from the file
def read_numbers_from_file(filename):
    try:
        with open(filename, "r") as input_file:
            numbers = []
            for line in input_file:
                numbers.append(line.strip())  # Strip newline characters and add to list
        return numbers
    except FileNotFoundError:
        exit()


# finds floats from the numbers list and puts in another list
def extract_floats(numbers):
    floats = []
    for element in numbers:
        try:
            num = float(element)
            floats.append(num)
        except ValueError:
            pass
    return floats


# function for printing values
def print_values(floats):
    for value in floats:
        print(round(value, 4), end=" ")
    print()


# function for printing the cumulative sum
def print_cumulative_sum(floats):
    cum_sum = 0
    for value in floats:
        cum_sum += value
        print(round(cum_sum, 4), end=" ")
    print()


# function for printing sorted values
def print_sorted_values(floats):
    floats.sort()
    for value in floats:
        print(round(value, 4), end=" ")
    print()


# function for printing the median+
def print_median(floats):
    if len(floats) > 0:
        print(round(statistics.median(floats), 4))


# open the file
filename = input("")
numbers = read_numbers_from_file(filename)
floats = extract_floats(numbers)

# prints values
print_values(floats)

# prints the cumulative sum
print_cumulative_sum(floats)

# prints values in ascending order
print_sorted_values(floats)

# prints the median
print_median(floats)
