QUIT = "q"

valid_passwords = 0
invalid_passwords = 0
total_passwords = 0

while True:
    password = input("Enter a password (or 'q' to quit): ")

    if password == QUIT:
        break

    total_passwords += 1

    if len(password) < 6 or len(password) > 20:
        print(f"{password}: Invalid length.")
        invalid_passwords += 1
        continue

    has_numeric = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)

    if not has_numeric:
        print(f"{password}: Missing numeric letter.")
        invalid_passwords += 1
        continue

    if not has_uppercase:
        print(f"{password}: Missing upper case letter.")
        invalid_passwords += 1
        continue

    if not has_lowercase:
        print(f"{password}: Missing lower case letter.")
        invalid_passwords += 1
        continue

    print(f"{password}: Valid password of length {len(password)}.")
    valid_passwords += 1

print(
    f"You tried {total_passwords} passwords, {valid_passwords} valid, {invalid_passwords} invalid."
)
