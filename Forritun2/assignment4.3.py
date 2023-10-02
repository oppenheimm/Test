size = int(input())
if size != 1:
    for i in range(size):
        if i == size - 1:
            print("*")
        else:
            print("*", end=" ")
    for i in range(size - 2):
        print("*", end=" ")
        for hj in range(size - 2):
            print(" ", end=" ")
        print("*")
    for i in range(size):
        if i == size - 1:
            print("*")
        else:
            print("*", end=" ")
else:
    print("*")
