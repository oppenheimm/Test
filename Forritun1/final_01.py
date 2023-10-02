# Author: <Tomas bragi thorvaldsson>
# Date: <21/4/2023>
# Project: <final_01>


class ShiftList(list):
    # doc string: this function rotates the list
    def shift(self, value):
        while value < 0:
            value += len(self)
        for i in range(value):
            self.insert(0, self.pop())


a = ShiftList()
sentance = input("sentance")
sent = sentance.split(" ")
for n in sent:
    a.append(n)
for n in sent:
    x = 0
    for t in n:
        if t.isupper():
            x = x
        else:
            x = x + 1


a.shift(x)
print(" ".join(a))
