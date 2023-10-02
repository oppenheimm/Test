n = int(input())

sequence = [1, 2, 3]

while len(sequence) < n:
    next_num = sum(sequence[-3:])
    sequence.append(next_num)

for num in sequence[:n]:
    print(num)

# hunk
