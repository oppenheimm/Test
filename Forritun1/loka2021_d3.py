valuelist = []

values = input("Enter board size and values: ")
valuelist = list(map(int, values.split()))

DIM = valuelist[0]


def print_board(board):
    """print board"""
    for i in range(DIM):
        # Print original board
        for j in range(DIM):
            if j > 0:
                print(" ", end="")
            print(board[i][j], end="")
        # Print line and mirrored board
        print(" | ", end="")
        for j in range(DIM):
            if j > 0:
                print(" ", end="")
            print(board[i][DIM - j - 1], end="")
        print()


def create_board():
    board = []
    for i in range(DIM):
        new_row = []
        for j in range(DIM):
            new_row.append(valuelist[(i * DIM) + j + 1])
        board.append(new_row)
    return board


board1 = create_board()
board2 = create_board()
print_board(board1)
print("-" * (DIM * 2 + 3))  # Print line separator
print_board(board2)

#######################################################################################


def create_matrix(size, elements):
    matrix = [[0] * size for _ in range(size)]
    idx = 0
    for i in range(size):
        for j in range(size):
            matrix[i][j] = elements[idx]
            idx += 1
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))
    print()


def mirror_matrix(matrix):
    size = len(matrix)
    mirrored = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            mirrored[i][j] = matrix[i][size - j - 1]
    return mirrored


def rotate_matrix(matrix):
    size = len(matrix)
    rotated = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rotated[i][j] = matrix[size - j - 1][i]
    return rotated


def main():
    input_str = input("Enter the size and elements of the matrix separated by spaces: ")
    input_list = list(map(int, input_str.split()))
    size = input_list[0]
    elements = input_list[1:]

    matrix = create_matrix(size, elements)
    print("Original matrix:")
    print_matrix(matrix)

    mirrored = mirror_matrix(matrix)
    print("Mirrored matrix:")
    print_matrix(mirrored)

    if size > 3:
        for i in range(4):
            matrix = rotate_matrix(matrix)
            print(f"Matrix rotated {90 * (i + 1)} degrees:")
            print_matrix(matrix)


if __name__ == "__main__":
    main()
