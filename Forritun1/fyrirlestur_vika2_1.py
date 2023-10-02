MIN_AGE = 17
MAX_AGE = 60

name = input("hvað heitru? ")
age = int(input("How old are you? "))

if age <0:
    print("haltu kjetti")
elif age >= MIN_AGE and age <= MAX_AGE:
    print("ert nogu gamall til að keyra")
elif age < MIN_AGE:
    print(f"sorry {name} ert ekki nogu gamal til að keyra ")
    print(f"you will have to wait for {MIN_AGE-age} ")
else:
    print(f"sorry {name} ert of gamal til að keyra ")
    print(f"attir að hætta keyra fyrir {age-MAX_AGE} ")
