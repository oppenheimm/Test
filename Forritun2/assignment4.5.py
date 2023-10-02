k = int(input())
n = int(input())
the_sum = 0
for i in range(n):
    x = int(input())
    if x > -1 and x < 2001:
        the_sum = the_sum + pow(k, x)
print(the_sum)
