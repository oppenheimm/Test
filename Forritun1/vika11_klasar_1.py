class ShiftList(list):
    def shift(self, value):
        while value < 0:
            value += len(self)
        for i in range(value):
            self.insert(0, self.pop())


a = ShiftList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
print(a)

a.shift(2)
print(a)

a.shift(-1)
print(a)

a.shift(-2)
print(a)

a.shift(23)
print(a)
