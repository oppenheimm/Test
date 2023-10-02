# Author: <Tomas Bragi Thorvaldsson> 
# Date: <2.17.2023> 
# Project: <midterm d2>


STOP_CRITERIA = "quit"

def get_input_email():
    return input('Email: ')

def print_results(CORRECT_COUNTER, INCORRECT_COUNTER):
    print(f'Total number of emails checked: {INCORRECT_COUNTER + CORRECT_COUNTER}')
    print(f'Number of valid emails:{CORRECT_COUNTER}')
    print(f'Number of invalid emails:{INCORRECT_COUNTER}')

CORRECT_COUNTER = 0
INCORRECT_COUNTER = 0

user_input = get_input_email()

while user_input != STOP_CRITERIA:
    if user_input[-4:] is ".org" or user_input[-4:] is ".com":
        for letter in enumerate(user_input):
            if letter == '@':
                CORRECT_COUNTER = CORRECT_COUNTER + 1
    else:
        INCORRECT_COUNTER = INCORRECT_COUNTER + 1
print_results(CORRECT_COUNTER, INCORRECT_COUNTER)





   
