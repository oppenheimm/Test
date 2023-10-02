class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares

    def __str__(self):
        return "{}: {}".format(self.symbol, self.shares)


class Portfolio:
    def __init__(self):
        self.stocks = []

    def add(self, stock):
        self.stocks.append(stock)

    def __str__(self):
        return "\n".join([str(stock) for stock in self.stocks])


stock1 = Stock("IBM", 100)
print(stock1)
stock2 = Stock("GOOG", 200)
stock3 = Stock("AMZN", 500)
portfolio = Portfolio()
portfolio.add(stock1)
portfolio.add(stock2)
portfolio.add(stock3)
print()
print(portfolio)
