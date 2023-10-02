def get_even_odd_num(thefile):
    odd_num = 0
    even_num = 0
    first_iteration = True

    for line in input_file:
        current = int(line)
        if current[-1:] == 0 or current[-1:] == 2 or current[-1:] == 4 or current[-1:] == 6 or current[-1:] == 8:
            even_num = even_num + 1
        else:
            odd_num = odd_num + 1

    return odd_num, even_num


filename = input('Filename: ')

try:
    input_file = open(filename,'w')

    odd_num, even_num = get_even_odd_num(input_file)        

    input_file.close()
    
    if odd_num > even_num:
        print("More odd than even numbers ")
    elif odd_num < even_num:
        print("More even than odd numbers ")
    else:
        print("Equal number of odd and even numbers")

except FileNotFoundError:
    print('File not found')