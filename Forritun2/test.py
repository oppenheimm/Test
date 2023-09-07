DIM = int(input())

board = []

# Create the board with '*' in all positions
for i in range(DIM):
    new_row = []
    for j in range(DIM):
        if i == DIM - 1 and j == DIM - 1:
            new_row.append("*")
        else:
            new_row.append("* ")
    board.append(new_row)

# Replace the interior '*' with spaces
for i in range(1, DIM - 1):
    for j in range(1, DIM - 1):
        board[i][j] = "  "

# Print the board
for i in range(DIM):
    for j in range(DIM):
        print(board[i][j], end="")
    print()
