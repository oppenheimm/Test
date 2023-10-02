rating = int(input())  # Do not change this line.

if rating >= 2700:
    print("Super grandmaster")
elif rating >= 2500:
    print("Grandmaster")
elif rating >= 2400:
    print("International grandmaster")
elif rating > 999:
    print("Amateur")
else:
    print("Invalid")
