

input_str = input('Write a sentence: ')

for letter in enumerate(input_str):
    if letter == '@':
        print("yubb")


def find_longest_word(the_file):
    even_num = 0
    odd_num = 0   

    for number in enumerate(input_str):
        if number/2 =
            print("yubb")

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