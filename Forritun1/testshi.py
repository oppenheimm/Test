import math


class SecondOrderPolynomial:
    def __init__(self, a=0, b=0, c=0):
        self._a = a
        self._b = b
        self._c = c

    def a(self):
        return self._a

    def b(self):
        return self._b

    def a(self):
        return self._c

    def __str__(self):
        return "{:.2f}x^2{:.2f}x{:.2f}".format(self._a, self._b, self._a)

    def evaluate(self, value):
        return (self._a * (value * value)) + (self._b * value) + self._c

    def roots(self):
        return (
            (
                -int(self._b)
                + math.sqrt(int(self._b) * 2 - 4 * int(self._a) * int(self._c))
            )
            / (2 * int(self._a)),
            (
                -int(self._b)
                - math.sqrt(int(self._b) * 2 - 4 * int(self._a) * int(self._c))
            )
            / (2 * int(self._a)),
        )

    def __add__(self, other):
        return SecondOrderPolynomial(
            self._a + other.a, self._b + other.b, self._c + other.c
        )

    def __mul__(self, value):
        return SecondOrderPolynomial(
            round(self._minutes * value),
            round(self._sms * value),
            round(self._gb * value),
        )

    def __eq__(self, other):
        return self._a, self._b, self._a == other.a, other.b, other.c


print("Testing f,g,h")
f = SecondOrderPolynomial()
g = SecondOrderPolynomial(2, 4, -3)
h = SecondOrderPolynomial(0, -3, 4)
print("f =", f)
print("g =", g)
print("h =", h)
print("Testing some combinations of coefficients")
print(SecondOrderPolynomial(0, 0, 7))
print(SecondOrderPolynomial(-1, -1, -1))
print(SecondOrderPolynomial(-2, 0, 0))
print(SecondOrderPolynomial(1, -1, 0))
print("Testing evaluations")
print("f(5) =", f.evaluate(5))
fg = f + g
print("f+g =", fg)
print("g*2 =", g * 2)
print("(g+h)*7 =", (g + h) * 7)
print("Testing roots")
print("g.roots:", g.roots())
f_sub_h = f - h
print("f-h =", f_sub_h)
print("f-h sum of roots =", sum(f_sub_h.roots()))
print("Checking equality")
if g == h:
    print(f"{g} and {h} are the same")
else:
    print(f"{g} and {h} are not the same")
if SecondOrderPolynomial(2, 4, -2) == SecondOrderPolynomial(1, 2, -1) * 2:
    print("Check!")
