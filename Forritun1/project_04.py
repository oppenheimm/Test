# Author: Tomas bragi Þorvaldsson, Bjarki Bjornsson, Larus Bergmann
# Date: 27/03/2023
# Project: Project4
# Acknowledgements: geeks for geeks hjalpaði með str functioninn og call function og finna inbyggð föll eins og __eq__. gat einnig spurt til broður mins þegar eg var i vafa. codebeutifully.org notað sem formatter.

# klasi fyrir klukku
class Clock:
    # þessi function setur gildi fyrir klukktima, minutur og sekundur
    def __init__(self, hrs=0, mins=0, secs=0):
        if isinstance(hrs, str):
            hrs, mins, secs = map(int, hrs.split(':'))

        self.hrs = (hrs + mins // 60 + secs // 3600) % 24
        self.mins = (mins + secs // 60) % 60
        self.secs = secs % 60


        self.hrs = hrs % 24
        self.mins = mins % 60
        self.secs = secs % 60

    # þessi function skilar streng ur clock hluta
    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hrs, self.mins, self.secs)

    # þessi function Stillir klukkutima
    def set_hours(self, hrs):
        self.hrs = hrs % 24

    # þessi function Stillir minutur
    def set_minutes(self, mins):
        self.mins = mins % 60
        self.set_hours(self.hrs + mins // 60)

    # þessi function Stillir sekundur
    def set_seconds(self, secs):
        self.secs = secs % 60
        self.set_minutes(self.mins + secs // 60)

    # þessi function sækir klukkutima gildið
    def hours(self):
        return self.hrs

    # þessi function sækir minutu gildið
    def minutes(self):
        return self.mins

    # þessi function sækir sekundu gildið
    def seconds(self):
        return self.secs

    # þessi function reiknar magn sekunda
    def total_sec(self):
        return self.hrs * 3600 + self.mins * 60 + self.secs

    # þessi function leggur saman tvo clock hluta og skilar nýjum clock hlut
    def __add__(self, values):
        total_sec = self.total_sec() + values.total_sec()
        hrs = total_sec // 3600 % 24
        xtra = total_sec % 3600
        mins = xtra // 60
        secs = xtra % 60
        return Clock(hrs, mins, secs)

    # þessi function dregur frá tvo clock hluta og skilar nýjum clock hlut
    def __sub__(self, values):
        total_sec = self.total_sec() - values.total_sec()
        hrs = total_sec // 3600
        xtra = total_sec % 3600
        mins = xtra // 60
        secs = xtra % 60
        return Clock(hrs, mins, secs)

    # þessi function margfaldar saman tvo clock hluta og skilar nýjum clock hlut
    def __mul__(self, value):
        total_sec = round(self.total_sec() * value)
        hrs = total_sec // 3600
        xtra = total_sec % 3600
        mins = xtra // 60
        secs = xtra % 60
        return Clock(hrs, mins, secs)

    # þessi function skoðar hvort einn clock hluti sé minni en annar
    def __lt__(self, values):
        return self.total_sec() < values.total_sec()

    # þessi function skoðar hvort einn clock hluti sé minni eða jafn öðrum
    def __le__(self, values):
        return self.total_sec() <= values.total_sec()

    # þessi function skoðar hvort tveir clock hlutar seu jafnir
    def __eq__(self, values):
        return self.total_sec() == values.total_sec()

    ## þessi function skoðar hvort tveir clock hlutar seu ekki jafnir
    def __ne__(self, values):
        return self.total_sec() != values.total_sec()

    # þessi function skoðar hvort einn clock hluti se stærri en annar
    def __gt__(self, values):
        return self.total_sec() > values.total_sec()

    # þessi function skoðar hvort einn clock hluti se stærri eða jafn öðrum
    def __ge__(self, values):
        return self.total_sec() >= values.total_sec()

    # þessi function updatear klukkutima minutur og sekundur clock hluta
    def __call__(self, argument):
        if len(argument) == 1:
            self.set_hours(argument[0])
        elif len(argument) == 2:
            self.set_hours(argument[0])



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