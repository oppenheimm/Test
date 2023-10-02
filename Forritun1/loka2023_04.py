class PhoneCard:
    def __init__(self, minutes=0, sms=0, gb=0):
        self.minutes = minutes
        self.sms = sms
        self.gb = gb

    def __str__(self):
        return "minutes= {:02.0f}, sms= {:02.0f}, data = {:02.0f}".format(
            self.minutes, self.sms, self.gb
        )

    def value(self):
        return self.minutes + self.gb + self.sms

    def __add__(self, other):
        return PhoneCard(
            self.minutes + other.minutes, self.sms + other.sms, self.gb + other.gb
        )

    def __mul__(self, value):
        return PhoneCard(
            round(self.minutes * value), round(self.sms * value), round(self.gb * value)
        )

    def __eq__(self, other):
        return self.value() == other.value()

    def __gt__(self, other):
        return self.value() > other.value()

    def make_a_call(self, call_duration):
        self.minutes -= call_duration

    def send_sms(self):
        self.sms -= 1

    def download(self, data_usage):
        self.gb -= data_usage


# You can keep your test cases below to test the corrected class


print("Testing init, str and value:")
e = PhoneCard()
print(e)
print()

x = PhoneCard(50, 50, 5)
print(x)
print("The value of the phonecard is", x.value())
print()

print("Testing plus and multiplication:")
y = x + x
print(y)
print("The value of the phonecard is", y.value())

z = y * 20
print(z)
print("The value of the phonecard is", z.value())
print()

print("Testing comparison:")
a = PhoneCard(0, 0, 5)
b = PhoneCard(47, 21, 3)
c = PhoneCard(50, 50, 0)
if b > a:
    print("Phonecard b is more valuable than phonecard a")
else:
    print("Phonecard a is at least as valuable as phonecard b")

if a == c:
    print("Phonecards a and c are identical")
else:
    print("Phonecards a and c are not identical")

if x == y * 0.5:
    print("Phonecard x is equal to half of phonecard y")
print()

print("Testing usage:")

print(x)

x.make_a_call(47)
for _ in range(23):
    x.send_sms()
x.download(3.5)

print(x)

x.make_a_call(17)
x.download(4.2)
x.send_sms()

print(x)
