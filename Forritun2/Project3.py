import math

stop_range = int(input())
num_divisors = int(input())

while (
    stop_range >= 20 and stop_range <= 100 and num_divisors >= 1 and num_divisors <= 12
):
    for i in range(stop_range):
        if (i % 10) + (((i) - (i % 10)) / 10) == math.sqrt(i):
            print(i)
100
