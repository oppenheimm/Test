def get_input():
    """this is a doc-string"""
    numbers = []
    
    current_input = input('Value: ')
    while current_input != 'quit': 
        current_number = int(current_input)
        
        numbers.append(current_number)
        
        current_input = input('Value: ')

    return numbers

numbers = get_input()

threshold = int(input('Threshold: '))

numbers_smaller = []
numbers_larger = []
for i in numbers:
    if i >= threshold:
        numbers_larger.append(i)
    elif i < threshold:
        numbers_smaller.append(i)

numbers_larger.sort()
numbers_smaller.sort()
numbers_smaller.reverse()

# prenta allar tölur minni en threshold í minnkandi röð
print(', '.join( [str(i) for i in numbers_smaller] ))

# prenta allar tölur stærri eða jafnt-og threshold í stækkandi röð
print(', '.join( [str(i) for i in numbers_larger] ))