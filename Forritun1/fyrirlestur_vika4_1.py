
s = input()
for i in range(1,len(s)):
    print(s[:1])
for i in range(len(s)):
    print(" "*i, end=" ")
    print(s[i:])

t = "this is a test to find all the i in the line"

while current_index >= 0:
    print(current_index)
    current_index = t.find("i", current_index + 1)
#?????

