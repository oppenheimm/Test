price = float(input())

total_price = 0.0
lowest_price = 1000
number_of_items = 0

while price != 0:
    total_price = total_price + price
    if price < lowest_price:
        lowest_price = lowest_price - (lowest_price - price)
    number_of_items = number_of_items + 1
    price = float(input())

print("Number of items:", number_of_items)
print("Total price:", round(total_price, 6))
if number_of_items > 0:
    print("Lowest price:", round(lowest_price, 4))
