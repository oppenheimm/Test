class Order:
    def __init__(self, item, price):
        self.__item = item
        self.__price = price

    def __str__(self):
        return "Item: {}, price: {}".format(self.item(), self.price())

    def __gt__(self, other):
        return self.price() > other.price()

    def __add__(self, other):
        new_item = self.item() + "+" + other.item()
        return Order(new_item, self.price() + other.price())

    def item(self):
        return self.__item

    def price(self):
        return self.__price


class TaxableOrder(Order):
    def __init__(self, item, price, tax):
        super().__init__(item, price)
        self.tax = tax

    def price(self):
        return round(super().price() + (super().price() * self.tax), 1)


def check_orders(order_list):
    for i in range(len(order_list) - 1):
        order1 = order_list[i]
        order2 = order_list[i + 1]
        if order1 > order2:
            print(
                "{} is more expensive ({}) than {} ({})".format(
                    order1.item(), order1.price(), order2.item(), order2.price()
                )
            )
        else:
            print(
                "{} is more (or equally) expensive ({}) than {} ({})".format(
                    order2.item(), order2.price(), order1.item(), order1.price()
                )
            )


# Main starts here
order1 = Order("iPhone", 1000.0)  # An order with item iPhone and the price 1000.0
order2 = Order("Kindle", 200.5)
order3 = Order("Samsung", 850.9)
# An order with the item Lenovo, the price 800.0 and 10% tax.
# The price with tax should be rounded to one decimal digit.
order4 = TaxableOrder("Lenovo", 800.0, 0.1)

order_list = [order1, order2, order3, order4]
for order in order_list:
    print(order)
check_orders(order_list)

order5 = order1 + order2
print(order5)
order6 = order5 + order4
print(order6)
