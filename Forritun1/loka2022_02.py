ROW = 4
LINE = 8
QUIT = "quit"
SEATS = 0


def print_board(board):
    for i in range(LINE):
        for j in range(ROW):
            if j > 0:
                print(" ", end="")
            print(board[i][j], end="")
            if j == 1:  # Add an extra space after seat 2 (index 1)
                print(" ", end="")
        print()


def create_board():
    board = []
    for i in range(LINE):
        new_row = []
        for j in range(ROW):
            new_row.append("_")
        board.append(new_row)
    return board


board = create_board()

print_board(board)

seat = input("Select a seat: ")
while seat != QUIT:
    line, row = seat.split(",")
    line = int(line)
    row = int(row)
    if board[line][row] != "X":
        board[line][row] = "X"
        SEATS = SEATS + 1
    else:
        print("sorry seat", line, row, "is taken")
    print_board(board)
    seat = input("Select a seat: ")

print("you booked", SEATS, "seats")
