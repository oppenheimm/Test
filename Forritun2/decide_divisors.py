def sum_of_divisors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum


def decide(num):
    sum = sum_of_divisors(num)
    if sum > num:
        return f"{num} is abundant."
    elif sum < num:
        return f"{num} is deficient."
    else:
        return f"{num} is a perfect number."
