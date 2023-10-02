def scramble_word(input_word):
    return input_word[-1] + input_word[1:-1] + input_word[0]


input_word = input("Write a word: ")

output_word = scramble_word(input_word)

print(output_word)


def count_case(text):
    upper_case_count = 0
    lower_case_count = 0
    for t in text:
        if t.isupper():
            upper_case_count += 1
        if t.islower():
            lower_case_count += 1
    return upper_case_count, lower_case_count


input_str = input("Enter a string: ")

upper_cases, lower_cases = count_case(input_str)

print("Upper case count:", upper_cases)
print("Lower case count:", lower_cases)


VOWELS = "aieou"


def pig_latin(input_word):
    if input_word[0] in VOWELS:
        return input_word + "yay"
    else:
        index = 0
        while input_word[index] not in VOWELS:
            index += 1
        return input_word[index:] + input_word[:index] + "ay"


input_word = input("Write a word: ")

print(pig_latin(input_word))
