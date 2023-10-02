def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"

    binary = ""

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal //= 2

    return binary
