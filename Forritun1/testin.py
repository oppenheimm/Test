class Clock:
    def __init__(self, hrs=0, mins=0, secs=0):
        if isinstance(hrs, str):
            hrs, mins, secs = map(int, hrs.split(':'))

        self.hrs = hrs % 24
        self.mins = mins % 60
        self.secs = secs % 60

    def __str__(self):
        return f"{self.hrs:02d}:{self.mins:02d}:{self.secs:02d}"

    def set_hours(self, hrs):
        self.hrs = hrs % 24

    def set_minutes(self, mins):
        self.mins = mins % 60

    def set_seconds(self, secs):
        self.secs = secs % 60

    def hours(self):
        return self.hrs

    def minutes(self):
        return self.mins

    def seconds(self):
        return self.secs

    def total_sec(self):
        return self.hrs * 3600 + self.mins * 60 + self.secs

    def __add__(self, values):
        total_sec = self.total_sec() + values.total_sec()
        return Clock(0, 0, total_sec)

    def __sub__(self, values):
        total_sec = self.total_sec() - values.total_sec()
        return Clock(0, 0, total_sec)

    def __mul__(self, value):
        total_sec = round(self.total_sec() * value)
        return Clock(0, 0, total_sec)

    def __lt__(self, values):
        return self.total_sec() < values.total_sec()

    def __le__(self, values):
        return self.total_sec() <= values.total_sec()

    def __eq__(self, values):
        return self.total_sec() == values.total_sec()

    def __ne__(self, values):
        return self.total_sec() != values.total_sec()

    def __gt__(self, values):
        return self.total_sec() > values.total_sec()

    def __ge__(self, values):
        return self.total_sec() >= values.total_sec()

    def __call__(self, args):
        if len(args) == 1:
            self.set_hours(args[0])
        elif len(args) == 2:
            self.set_hours(args[0])
            self.set_minutes(args[1])
        elif len(args) == 3:
            self.set_hours(args[0])
            self.set_minutes(args[1])
            self.set_seconds(args[2])


print('Testing initialization:')
a = Clock()
b = Clock('12:23:53')
c = Clock(18,3,21)
print('a =', a)
print('b =', b)
print('c =', c)
print()
print('Testing set functions:')
d = Clock()
d.set_hours(37)
d.set_minutes(142)
d.set_seconds(938)
print('d =', d)
print()
print('Testing addition, subtraction and multiplication')
e = b + c
print('e = b + c =', e)
f = e - b
print('f = e - b =', f)
g = b * 0.8
h = d * 2
print('g = b * 0.8 =', g)
print('h = d * 2 =', h)
print()
print('Test get functions')
print('e =', e)
print('e.hours() =', e.hours())
print('e.minutes() =', e.minutes())
print('e.seconds() =', e.seconds())
print()
print('Testing comparisons:')
i = Clock(6,27,13)
if i < e:
    print(i,'<',e)
if b > g:
    print(b,'>',g)
if c == f:
    print(c, '==', f)
if c >= c:
    print(c, '>=', c)
if b <= c:
    print(b, '<=', c)
