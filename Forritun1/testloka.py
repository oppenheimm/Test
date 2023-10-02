valuelist = []

values = input("Enter board size and values: ")
valuelist = list(map(int, values.split()))

DIM = valuelist[0]
DIMLO = valuelist[0] * 2


def print_board(board):
    """print board"""
    for i in range(DIM):
        for j in range(DIM):
            if j > 0:
                print(" ", end="")
            print(board[i][j], end="")
        print()


def create_board():
    board = []
    for i in range(DIM):
        new_row = []
        for j in range(DIM):
            new_row.append(valuelist[i * DIM + j + 1])
        board.append(new_row)
        for i in range(DIMLO):
            new_row = []
        for j in range(DIM):
            new_row.append(valuelist[i * DIM + j + 1])
        board.append(new_row)
    return board


board = create_board()

print_board(board)
