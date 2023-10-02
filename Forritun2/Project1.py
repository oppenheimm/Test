symbol = input("The stock symbol:\n")
shares = int(input("Number of shares:\n"))
buy_price = float(input("The stock buying price:\n"))
sell_price = float(input("The stock selling price:\n"))

payment = shares * buy_price
sold = shares * sell_price
buy_com = payment * 0.03
sell_com = sold * 0.03
pl = sold - payment - sell_com - buy_com

print("Transactions for stock:", symbol)
print("Bought", shares, "shares @", buy_price)
print("Paid", round(payment, 2))
print("Commission when buying:", round(buy_com, 2))
print("Sold", shares, "shares @", sell_price)
print("Received", round(sold, 2))
print("Commission when selling:", round(sell_com, 2))
print("Profit or loss:", round(pl, 2))
