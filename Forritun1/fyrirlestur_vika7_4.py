import random

#function annotation example
def find_second_largest_v1(current_list: list) -> int:
    second_largest = sorted(current_list)[-2]
    return second_largest


def find_second_largest_v2(current_list):
    current_list.sort()
    second_largest = current_list[-2]
    return second_largest

def find_some_largest_value(current_list, nr_order = 2):
    return_value = sorted(current_list)[-1*nr_order]
    return return_value

the_list = []
for _ in range(20):
    the_list.append( random.randint(0,100) )

print(the_list)
print(find_some_largest_value(the_list, nr_order = 4))
print(the_list)