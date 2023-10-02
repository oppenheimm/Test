# asks for input
stop_range = int(input())
num_divisors = int(input())

# Finds and prints all positive two digit integers strictly less than stop_range, whose square of the sum of its digits is equal to the original integer.
for i in range(stop_range):
    if i > 20 and i < 100:
        if ((i // 10) + ((i % 10))) ** 2 == i:
            print(i)

# Finds and prints all positive integers strictly less than stop_range, with exactly num_divisors positivedivisors.
if num_divisors > 2 and num_divisors < 12:
    for i in range(1, stop_range):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == num_divisors:
            print(i)
