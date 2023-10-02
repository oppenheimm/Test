year = int(input())

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")
