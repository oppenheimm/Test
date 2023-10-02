# Author: tomas bragi thorvaldsson
# Date: 3/26/2023
# Project: assignment_06_01
# Acknowledgements:geeks4geeks með svipað dæmi

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name}: {self.price}"

class Portfolio:
    def __init__(self):
        self.stocks = []
        
    def add(self, stock):
        self.stocks.append(stock)
        
    def __str__(self):
        result = ""
        for stock in self.stocks:
            result += f"{str(stock)}\n"
        return result

