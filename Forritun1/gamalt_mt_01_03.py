QUIT = "quit"

starting_position = input("starting position (x,y): ")
x, y = starting_position.split(",")
x = int(x)
y = int(y)
movement = input("move: ")

while movement != QUIT:
    movement = movement.lower()
    if movement == "u":
        y = y + 1
    elif movement == "d":
        y = y - 1
    elif movement == "r":
        x = x + 1
    elif movement == "l":
        x = x - 1

    movement = input("move: ")

print("final position", x, ",", y)
