def extract_first_number_from_string(input_string):
    str = ""
    is_num = False

    for char in input_string:
        if char.isdigit():
            str += char
            is_num = True
        elif is_num:
            break

    if str:
        return int(str)
    else:
        return -1
