#Write a Python program that reads a file, whose name is input by the user, containing one 
#word/token per line with an empty line between sentences.  The program prints out the 
#longest word found in the file along with its length. If the input file is not found (use try-
#except), the program should print "File not found".  If there is a tie, the program should use 
#the first longest word it finds. 


def find_longest_word(the_file):
    longest_word = ''
    max_length = 0   

    for line in input_file:
        if len(line) > max_length:
            max_length = len(line.strip())
            longest_word = line.strip()

    return longest_word, max_length


filename = input('Filename: ')



try:
    input_file = open(filename,'r')

    longest_word, max_length = find_longest_word(input_file)

    input_file.close()
    
    print(longest_word)
    print(max_length,'letters')

except FileNotFoundError:
    print('File not found')

##########################################################################
#Write a Python program that reads a file, whose name is input by the user.  The contents of 
#the file is either a number or a word in each line.  The program should print out all the 
#numbers in the file, i.e. effectively removing the text from the file.  You should use try-
#except to see if the contents of a line is a number or a text.  If the file doesn't exist, the 
#program should print out "File not found".  Your program should have at least two 
#functions. 



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


################################################################################
#Write a program that reads a file, whose name is input by the user, and prints out the 
#contents after removing all spaces and newlines. Punctuations will be preserved. 


filename = input('Filename: ')

input_file = open(filename, 'r')

compressed_text = ''

for line in input_file:
    compressed_text += line.strip().replace(' ','')

print(compressed_text)

input_file.close()

##################################################################################

#Write a Python program that reads a file, whose name is input by the user.  The contents of 
#the file are numbers, one number in each line.  The program should print out the minimum 
#and maximum numbers, as well as the average of all the numbers. If the file doesn't exist, 
#the program should print out "File not found".  
#The program should include a function that calculates the min, max and average.




def get_min_max_average(thefile):
    largest_number = 0
    smallest_number = 0
    sum_of_numbers = 0
    count_of_numbers = 0
    first_iteration = True

    for line in input_file:
        current = float(line)
        if current > largest_number or first_iteration:
            largest_number = current
        if current < smallest_number or first_iteration:
            smallest_number = current
        sum_of_numbers += current
        count_of_numbers += 1
        first_iteration = False

    return largest_number, smallest_number, sum_of_numbers / count_of_numbers


filename = input('Filename: ')

try:
    input_file = open(filename,'r')

    largest_number, smallest_number, average = get_min_max_average(input_file)        

    input_file.close()
    
    print('Maximum:', largest_number)
    print('Minimum:', smallest_number)
    print('Average:', average)

except FileNotFoundError:
    print('File not found')

############################################################+
x = 1 , 3 , 5 
print(x)
print(type(x))