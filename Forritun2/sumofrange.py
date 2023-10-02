def sum_of_range(start, end, step):
    total_sum = 0

    for i in range(start, end + 1, step):
        total_sum += i

    return total_sum
