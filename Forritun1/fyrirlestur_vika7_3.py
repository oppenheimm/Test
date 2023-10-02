# Prenta:
# OOOO
# OOOO
# OOOO
# OOOO
# notandi velur reit, breyta reit úr O í X, eða úr X í O

WIIDTH = 4
LENGTH = 8
def print_board( board ):
    for i in range(LENGTH):
        for j in range(WIIDTH):
            print(board[i][j],end='')
        print()
    
def create_board():
    board = []
    for _ in range(LENGTH):
        sub_list = []
        for _ in range(WIIDTH):
            sub_list.append( '_' )
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