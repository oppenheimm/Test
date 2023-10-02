def is_float(s):
    try:
        f = float(s)
        return True
    except ValueError:
        return False


def print_numbers_from_file(the_file):
    for line in the_file:
        if is_float(line.strip()):
            print(line.strip())    


filename = input('Filename: ')

try:
    input_file = open(filename, 'r')

    print_numbers_from_file(input_file)

    input_file.close()

except FileNotFoundError:
    print('File not found')