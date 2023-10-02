# ----------------- Constants -----------------

STOP_CRITERIA = 'quit'

# ----------------- Functions -----------------

def get_input_equation():
    """Get an input from the user"""
    return input('Equation: ')

def parse_equation(equation):
    """Parse the input from the user, read the elements of the equation"""
    a,action,b,equality,c = user_input.split()
    return int(a), int(b), int(c), action

def check_equation(a,b,action):
    """Check if the equation action is valid and return the correct answer"""
    if action == 'x':
        return True, a * b
    elif action == '//':
        return True, a // b
    elif action == '+':
        return True, a + b
    elif action == '-':
        return True, a - b
    elif action == '%':
        return True, a % b
    else:
        return False, -1

def print_correct():
    """Print correct"""
    print('Correct')

def print_wrong(a, b, answer, action):
    """Print out the correct answer, used when user gave an incorrect equation"""
    print(f'Sorry, {a} {action} {b} = {answer}')

def print_syntax_error():
    """Print out an error message"""
    print("Sorry, I don't understand this equation")

def print_results(correct_answers, wrong_answers):
    """Print out the final result"""
    print(f'You tried {wrong_answers + correct_answers} equations.')
    print(f'You got {correct_answers} correct and {wrong_answers} wrong.')


# ----------------------- Main part starts here --------------------

correct_answers = wrong_answers = 0

user_input = get_input_equation()

while user_input != STOP_CRITERIA:
    a, b, c, action = parse_equation(user_input)

    equation_is_ok, correct_answer = check_equation(a, b, action)

    if equation_is_ok and correct_answer == c:
        print_correct()
        correct_answers += 1
    elif equation_is_ok and correct_answer != c:
        print_wrong(a, b, correct_answer, action)
        wrong_answers += 1
    else:
        print_syntax_error()

    user_input = get_input_equation()

print_results(correct_answers, wrong_answers)

