filename = r"C:\Users\Tommi\Forritun Visual stud\project_03_extra_files\small_locations.txt"
the_file = open(filename, 'r')
lines = the_file.readlines()

def second_smallest(numbers):
    m1 = m2 = float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

result = []
for i, line in enumerate(lines):
    numbers = [int(n) for n in line.strip().split()]
    second_smallest_value = second_smallest(numbers)
    result.append([i, second_smallest_value])

print(result)
