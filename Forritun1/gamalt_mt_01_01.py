QUIT = "quit"

# liklegast betra að bara sleppa functions#


def payment(quant, price):
    try:
        pay = int(quant) * int(price)
        print("total price:", pay)
        if pay > 10000:
            pay = pay * 0.9
            print("discounted price: ", pay)
        return pay
    except ValueError:
        print("Invalid input. Please try again.")
        return 0


total_payment = 0

while True:
    quant = input("quantity: ")
    if quant.lower() == QUIT:
        break
    price = input("price: ")
    if price.lower() == QUIT:
        break

    total_payment += payment(quant, price)

print("Total payment:", total_payment)
