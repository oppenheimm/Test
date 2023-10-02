name = input("")

first, last = name.split(", ")

new_name = last[0].upper() + ". " + first.capitalize()

print(new_name)
