mb_per_month = int(input())
n = int(input())

lim = (n * mb_per_month) + mb_per_month
total_usage = 0
for i in range(n):
    usage = int(input())
    total_usage = total_usage + usage
print(lim - total_usage)
