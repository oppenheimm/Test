DIM = 9

def print_board(board):
    """print board"""
    for i in range(DIM):
        for j in range(DIM):
            if j > 0:
                print(' ', end='')
            print(board[i][j], end='')
        print()

def create_board():
    board = []
    for i in range(DIM):
        new_row = []
        for j in range(DIM):
            new_row.append('_')
        board.append(new_row)
    return board

board = create_board()

#Testing how the board works
#board[2][7] = 'X'
#board[0][0] = '?'
#board[8][8] = '$'
#print_board(board)

filename = 'sudoku_v1.txt'
the_file = open(filename, 'r')
the_data = the_file.readlines()
the_file.close()

for line in the_data:
    a,b,c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    board[a-1][b-1] = c

print_board(board)