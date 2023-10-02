# Author: <Tómas Bragi Þorvaldsson> 
# Date: <2.1.2023> 
# Project: <skilaverk 3 d 2> 
# Acknowledgements: inspo fyrir function á stackoverflow og vann með ivari


def reverse(x):
    return x[0] + x[1:-1][::-1] + x[-1]

while True:
    x = input("Input: ")
    if x == 'quit':
        break
    reversed_word = reverse(x)
    print(reversed_word)

