string = input("").lower()
reverse_string = string[::-1]
if string == reverse_string:
    print("Palindrome!")
else:
    print("Nothing special about this string :(")
