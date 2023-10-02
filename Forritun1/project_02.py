# Author: <Tómas Bragi Þorvaldsson> 
# Date: <2.1.2023> 
# Project: <Math equations> 
# Acknowledgements: stackoverflow fyrir tips og https://realpython.com/regex-python/ fyrir regex function

import re

#this functions takes the equation input and splits it into terms and a operator using regex
def parse(equation_input) -> list[str]:
    if not equation_input and not isinstance(equation_input, str):
        return []
    pattern = r'(?P<first_term>\d+)\s*(?P<operator>\+|x|%|-|//)\s*(?P<second_term>\d+)\s*(?P<equals>=)\s*(?P<result>\d+)'
    match = re.search(pattern, equation_input)
    if match is None:
        print("Sorry, I don't understand this equation")
        return []
    return [match.group('first_term'), match.group('operator'), match.group('second_term'), match.group('equals'), match.group('result')]

#this function adds two numbers
def add(x, y):
    return x + y

#this function subtracts two numbers
def subtract(x, y):
    return x - y

#this function multiplys two functions
def multiply(x, y):
    return x * y

#this function divides two numbers
def divide(x, y):
    return x / y

#this function % two numbers
def perc(x, y):
    return x % y


COUNTER = 0
CORRECT_COUNTER = 0
INCORRECT_COUNTER = 0

while True:
    equation_input = input("Equation: ")
    if equation_input == 'quit':
        print("You tried",COUNTER,"equations.")
        print("You got",CORRECT_COUNTER,"correct and",INCORRECT_COUNTER,"wrong.")
        break
    else:
        equation = parse(equation_input)
        if not equation:
            continue
    
        first_term = int(equation[0])
        operator = equation[1]
        second_term = int(equation[2])
        final_term = int(equation[4])
    
        if operator == '+':
            action = add(first_term,second_term)
        elif operator == '-':
            action = subtract(first_term,second_term)
        elif operator == 'x':
            action = multiply(first_term,second_term)
        elif operator == '//':
            action = int(divide(first_term,second_term))
        elif operator == '%':
            action = int(perc(first_term,second_term))

        if  action == final_term:
            print("Correct")
            CORRECT_COUNTER = CORRECT_COUNTER + 1
            COUNTER = COUNTER + 1
        else:
            print("Sorry,",first_term, operator ,second_term,"=",int(action))
            INCORRECT_COUNTER = INCORRECT_COUNTER + 1
            COUNTER = COUNTER + 1

