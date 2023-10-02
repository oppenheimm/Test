answer = input("You need something doubled? (Y)es?\n")

YES = "Y"


while answer == YES:
    number = float(
        input("All right, then. Give me a number, and I'll double it for ya:\n")
    )
    print(number * 2)
    answer = input("You need something else doubled? (Y)es?\n")
