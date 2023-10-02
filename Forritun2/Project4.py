password = input("")

QUIT = "q"

# counters for valid , invalid and total inputs
valid_passwords = 0
invalid_passwords = 0
total_passwords = 0

while password != QUIT:
    total_passwords = total_passwords + 1
    if (
        len(password) >= 6 and len(password) <= 20
    ):  # if all these requirements are true program prints the length of input asks for another input
        if True in [char.islower() for char in password]:
            if True in [char.isupper() for char in password]:
                if True in [char.isdigit() for char in password]:
                    print(f"{password}: Valid password of length {len(password)}.")
                    valid_passwords = valid_passwords + 1
                    password = input("")
                else:
                    print(f"{password}: Missing numeric letter.")
                    invalid_passwords = invalid_passwords + 1
                    password = input("")
            else:  # if upper case is missing the program finds if anything is missing then asks for new input
                print(f"{password}: Missing upper case letter.")
                invalid_passwords = invalid_passwords + 1
                if True in [char.isdigit() for char in password]:
                    pass
                else:
                    print(f"{password}: Missing numeric letter.")
                password = input("")
        else:  # if lower case is missing the program finds if anything else is missing then asks for new input
            print(f"{password}: Missing lower case letter.")
            invalid_passwords = invalid_passwords + 1
            if True in [char.isupper() for char in password]:
                pass
            else:
                print(f"{password}: Missing upper case letter.")
            if True in [char.isdigit() for char in password]:
                pass
            else:
                print(f"{password}: Missing numeric letter.")
            password = input("")
    else:  # if length is invalid it asks for new input
        print(f"{password}: Invalid length.")
        invalid_passwords = invalid_passwords + 1
        password = input("")

print(
    f"you tried {total_passwords} passwords, {valid_passwords} valid, {invalid_passwords} invalid."
)
