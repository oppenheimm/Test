income = int(input("Income: "))

while income >= 0:

    canada = float(income*0.26)

    if income <= 3000:
        norway = float(income*0.1)
    else:
        norway = float((income-3000)*0.4)+(3000*0.1)

    y = 0.1
    if income <= 1000:
        denmark = float(0)
    else:
        denmark = 0
        while (income-1000) >= y*10000:
            denmark = float(denmark+(((income-((income-1000)))*y))+(y*(income-(int(income/1000)*1000))))
            y += 0.1

    if income <= 1500:
        Us = float(income*0.12)
    elif income > 1500 and income <= 6000:
        Us = float(income*0.25)
    elif income > 6000 and income <= 10000:
        Us = float(income*0.38)
    else:
        Us = float(income*0.15)

    lowest_tax = min(Us, norway, denmark, canada)
    print("Lowest tax:",lowest_tax)
    if Us == lowest_tax:
        print("USA")
    if norway == lowest_tax:
        print("Norway")
    if denmark == lowest_tax:
        print("Denmark")
    if canada == lowest_tax:
        print("Canada")

    income = int(input("Income: "))
