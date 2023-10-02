import cmath

a = float(input('Coefficient a: '))
b = float(input('Coefficient b: '))
c = float(input('Coefficient c: '))

d = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(d))/(2*a)
root2 = (-b - cmath.sqrt(d))/(2*a)

print('Polynomial: ', a, 'x^2 + ', b, 'x + ', c)
print('Root 1:', root1)
print('Root 2:', root2)