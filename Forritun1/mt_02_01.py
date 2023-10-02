import math

valuelist = []

values = input("Numbers: ")
valuelist = list(map(int, values.split()))

DIM = int(math.sqrt(len(valuelist)))


def print_board(board):
    """print board"""
    for i in range(DIM):
        # Print original board
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
            new_row.append(valuelist[i * DIM + j])
        board.append(new_row)
    return board


def is_symmetric(board):
    symmetric = True
    for i in range(DIM):
        for j in range(DIM):
            if board[i][j] != board[j][i]:
                symmetric = False
    return symmetric


board = create_board()
print_board(board)

if is_symmetric(board):
    print("Symmetric!")
