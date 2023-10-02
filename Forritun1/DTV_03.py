input_str = input('Write a sentence: ')

for index, letter in enumerate(input_str):
    if letter == 'e':
        print(index)
########################################################################


top_num = int(input('Upper number for the range: ')) 

for n in range(1,top_num+1):
    sum_of_factors = 0

    for j in range(1,n):
        if n % j == 0:
            sum_of_factors += j

    if sum_of_factors == n:
        print(n)
#########################################################################



    input_str = input('Write a word: ') 

for i in range(1,len(input_str)):
    print(input_str[:i]) 

for i in range(len(input_str)):
    print(' '*i, end='')
    print(input_str[i:])
############################################################################


    c_max = int(input('Upper limit for the longest side: ')) # Do not change this line

for a in range(1,c_max):
    for b in range(a,c_max):
        for c in range(b,c_max+1):
            if a**2 + b**2 == c**2:
                print(a,b,c)


