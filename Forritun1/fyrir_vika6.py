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

############################################Svipað dæmi, bara aðeins meira sem við gerum við tölurnar

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

###############################################Dæmi um notkun á tvívíðum listum

# Prenta:
# OOOO
# OOOO
# OOOO
# OOOO
# notandi velur reit, breyta reit úr O í X, eða úr X í O

SIZE = 4

def print_board( board ):
    for i in range(SIZE):
        for j in range(SIZE):
            print(board[i][j],end='')
        print()
    
def create_board():
    board = []
    for _ in range(SIZE):
        sub_list = []
        for _ in range(SIZE):
            sub_list.append( 'O' )
        board.append( sub_list )
    return board

board = create_board()
print_board(board)

user_input = input('Tile: ')
while user_input != 'quit':
    # user_input: 2 1
    row, col = user_input.split()
    row = int(row)
    col = int(col)

    board[row][col] = 'X'    
    
    print()
    print_board(board)

    user_input = input('Tile: ')
