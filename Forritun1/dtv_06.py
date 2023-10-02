def get_unique_letters(sentence):
    unique_letters = []
    for ch in sentence:
        ch = ch.lower()
        if ch not in """.,;?!-'"(): """ and ch not in unique_letters:
            unique_letters.append(ch)
    return unique_letters

# main program starts here
sentence = input("Input a sentence: ")
unique_letters = get_unique_letters(sentence)
print("Unique letters:", ''.join(sorted(unique_letters)))

##############

def calculate_score(scores):
    return (sum(scores) - min(scores) - max(scores)) / (len(scores)-2)

input_str = input('Enter scores separated by space: ')

scores = [float(x) for x in input_str.split()]

mean = calculate_score(scores)

print('Score = {}'.format(round(mean,2)))

################

def first_and_last_char_same(word_list):
    '''Returns a new list containing the words from word_list that begin and end with the same char'''
    result_list = []
    for word in word_list:
        if len(word) > 1 and word[0] == word[-1]:
            result_list.append(word)
    return result_list

def read_string():
    '''Prompts for an input string and returns it'''
    input_str = input('Enter word to be added to list: ')
    return input_str

def populate_list(a_list):
    '''Populates a_list with words until the user inputs "q"'''
    a_string = read_string()
    while a_string != 'q':
        a_list.append(a_string)
        a_string = read_string()

def print_list(a_list):
    s = ''
    for item in a_list:
        if len(s) > 0:
            s += ', '
        s += item
    print(s)

# Main program starts here
initial_list = []
populate_list(initial_list)
print_list(initial_list)
new_list = first_and_last_char_same(initial_list)
print_list(new_list)

###############

def dot_product(vector1, vector2):
    '''Calculate the dot product between two vectors'''
    dot_result = 0
    for i in range(len(vector1)):
        dot_result += vector1[i]*vector2[i]
    return dot_result

def vector_string_to_list(vector_str):
    '''Takes a vector as a string and returns the vector as a list of floats'''
    return [float(x) for x in vector_str.split()]

vector1_str = input('Vector 1: ')
vector2_str = input('Vector 2: ')

vector1 = vector_string_to_list(vector1_str)
vector2 = vector_string_to_list(vector2_str)

v1_dot_v2 = dot_product(vector1, vector2)

print('The dot product is:', v1_dot_v2)