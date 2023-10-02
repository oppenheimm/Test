# Author: Tomas bragi
# Date: 2/26/2023
# Project: skilaverk 4 dæmi 4
# Acknowledgements: byggt mikið á á fyrirlestrardæmi í viku 7

WIIDTH = 4
LENGTH = 8

seatcounter = 0

def print_board(board):
    for i in range(LENGTH):
        for j in range(WIIDTH):
            print(board[i][j], end='')
        print()

def create_board():
    board = []
    for _ in range(LENGTH):
        sub_list = []
        for _ in range(WIIDTH):
            sub_list.append('_ ')
        board.append(sub_list)
        sub_list[1] = "_   "
    return board

def check_seat(board, row, col):
    if board[row][col] == 'X ' or board[row][col] == "X   ":
        print("Sorry, seat",col,"in row",row,"is occupied.")
        print_board(board)
        return False
    else:
        return True

board = create_board()
print_board(board)

user_input = input('Select a seat: ')
while user_input != 'quit':
    row, col = user_input.split(",")
    row = int(row)
    col = int(col)

    if check_seat(board, row, col):
        if col == 1:
            board[row][col] = 'X   ' 
            print("Seat",col,"in row",row,"is now booked.")
            print_board(board)
        else:
            board[row][col] = 'X ' 
            print("Seat",col,"in row",row,"is now booked.")
            print_board(board)

        seatcounter = seatcounter + 1
    user_input = input('Select a seat: ')
print("You booked",seatcounter,"seats.")