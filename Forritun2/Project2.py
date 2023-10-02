grades = []
credits = []

while True:
    grade = float(input())

    if grade < 0:
        break

    credit = int(input())

    grades.append(grade)
    credits.append(credit)

if sum(grades) > 0:
    if sum(credits) != 0:
        weight = [a * b for a, b in zip(grades, credits)]
        wag = round(sum(weight) / sum(credits), 2)
        print("Weighted average grade:", wag)

    highest_grade = max(grades)
    if highest_grade >= 0:
        print("Highest grade:", highest_grade)
