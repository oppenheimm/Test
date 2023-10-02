# Author: <Tomas bragi thorvaldsson>
# Date: <21/4/2023>
# Project: <final_04>

import math


class SecondOrderPolynomial:
    # this function sets values for a,b,c
    def __init__(self, a=0, b=0, c=0):
        self._a = int(a)
        self._b = int(b)
        self._c = int(c)

    # returns a
    def a(self):
        return self._a

    # returns b
    def b(self):
        return self._b

    # returns c
    def a(self):
        return self._c

    # returns string
    def __str__(self):
        return "{:.2f}x^2{:.2f}x{:.2f}".format(self._a, self._b, self._a)

    # evaluates the formula
    def evaluate(self, value):
        return (self._a * (value * value)) + (self._b * value) + self._c

    # finds roots
    def roots(self):
        if (2 * self._a) != 0:
            return (
                (-self._b + math.sqrt(self._b * 2 - 4 * self._a * self._c))
                / (2 * self._a),
                (-self._b - math.sqrt(self._b * 2 - 4 * self._a * self._c))
                / (2 * self._a),
            )
        else:
            return (0, 0)

    # adds two functions
    def __add__(self, other):
        return SecondOrderPolynomial(
            self._a + other._a, self._b + other._b, self._c + other._c
        )

    # subtracts two functions
    def __sub__(self, other):
        return SecondOrderPolynomial(
            self._a - other._a, self._b - other._b, self._c - other._c
        )

    # multiplys a function with a value
    def __mul__(self, value):
        return SecondOrderPolynomial(
            round(self._a * value),
            round(self._b * value),
            round(self._c * value),
        )

    # checks if functions are equal
    def __eq__(self, other):
        return self._a, self._b, self._a == other._a, other._b, other._c


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
