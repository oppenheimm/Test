class OrderedPair:
    def __init__(self, x=0, y=0):
        self.x = min(x, y)
        self.y = max(x, y)

    def set_element(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        else:
            raise IndexError("Index out of range")
        self.x, self.y = min(self.x, self.y), max(self.x, self.y)

    def __add__(self, other):
        return OrderedPair(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return OrderedPair(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ge__(self, other):
        return self.x + self.y >= other.x + other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


print("----- testing init ----------")
a = OrderedPair()
print("a =", a)

b = OrderedPair(2, 4)
print("b =", b)

c = OrderedPair(5, 3)
print("c =", c)

print("------- testing set element ----------")
# set_element fallið tekur inn index og gildi
# þ.e. set_element(0,8) segir að við eigum að breyta gildinu á fyrra stakinu í 8
a.set_element(0, 8)
print("a(0) = 8")
print("a =", a)
a.set_element(0, 4)
print("a(0) = 4")
print("a =", a)
a.set_element(1, 3)
print("a(1) = 3")
print("a =", a)

print("-------- testing plus and minus ---------")
d = a + b
print("a + b =", d)

e = b - a
print("b - a =", e)

print("-------- testing equal and greater-than-or-equal ---------")
# Samanburður virkar þannig að við leggjum saman tölurnar og berum saman summu þeirra
if e >= d:
    print(e, ">=", d)
else:
    print(e, "<", d)

# Tvö OrdererdPair er eins ef þau innihalda sömu tölur.
if b == c:
    print(b, "and", c, "are equal")
else:
    print(b, "and", c, "are not equal")

if b == OrderedPair(4, 2):
    print(b, "is (2,4)")
