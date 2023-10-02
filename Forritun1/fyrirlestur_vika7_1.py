def get_sorted_input():
    """this is a doc-string"""
    numbers = []
    
    current_input = input('Value: ')
    while current_input != 'quit': 
        current_number = int(current_input)
        
        numbers.append(current_number)
        
        current_input = input('Value: ')

    return sorted(numbers)

numbers = get_sorted_input()


str_numbers = []
for i in numbers:
    str_numbers.append(str(i))
print(', '.join(str_numbers))

# another way
print(', '.join( [str(i) for i in numbers] ))