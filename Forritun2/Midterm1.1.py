piece = int(input())

if piece == 9:
    print("Queen")
elif piece == 5:
    print("Rook")
elif piece == 3:
    print("Bishop or Knight")
elif piece == 1:
    print("Pawn")
else:
    print("No piece")
