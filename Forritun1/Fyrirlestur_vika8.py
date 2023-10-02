#############################Að telja orð með listum:

import string

def clean_word(word):
    return word.strip(string.punctuation)    

the_words = []
the_count = []

filename = 'test.txt'
the_file = open(filename,'r')

for line in the_file:
    words = line.lower().split()
    for w in words:
        w = clean_word(w)
        if w in the_words:
            i = the_words.index(w)
            the_count[i] += 1
        else:
            the_words.append(w)
            the_count.append(1)

the_file.close()

for i in range(len(the_words)):
    print(the_words[i], the_count[i])


 

####################Að telja orð með uppflettitöflu:

import string

def clean_word(word):
    return word.strip(string.punctuation)    

the_words = {}

filename = 'shakespeare_all.txt'
#filename = 'grimm.txt'
the_file = open(filename,'r')

for line in the_file:
    words = line.lower().split()
    for w in words:
        w = clean_word(w)

        if w not in the_words:
            the_words[w] = 0

        the_words[w] += 1

        """
        if w in the_words:
            the_words[w] += 1
        else:
            the_words[w] = 1
        """
       
the_file.close()

the_list = []
for k,v in the_words.items():
    the_list.append( (v,k) )

the_list.sort()
the_list.reverse()

for i in range(20):
    print( the_list[i][1], the_list[i][0] )

    def calculate_gpa_long_version(course_grades):
    #"""grades is a dict, assignments as keys and grades as values"""
    total_grade = 0
    number_of_grades = 0
    for assignment, grade in course_grades.items():
        total_grade += grade
        number_of_grades += 1
    return total_grade/number_of_grades

def calculate_gpa(course_grades):
    #"""grades is a dict, assignments as keys and grades as values"""
    return sum(course_grades.values())/len(course_grades)

students = {}

filename = 'students.txt'
the_file = open(filename, 'r')
for line in the_file:
    userid, fullname, address, kt = line.strip().split(',')
    # Uppflettitafla með upplýsingum um nemanda
    students[userid] = {}
    students[userid]['Name'] = fullname
    students[userid]['Address'] = address
    students[userid]['SSN'] = kt
    students[userid]['Courses'] = {}
the_file.close()

filename = 'student_grades.txt'
the_file = open(filename, 'r')
for line in the_file:
    userid,courseid,assignment,grade = line.strip().split(',')

    if courseid not in students[userid]['Courses']:
        students[userid]['Courses'][courseid] = {}

    students[userid]['Courses'][courseid][assignment] = float(grade)
the_file.close()

for userid,info in students.items():
    print(userid)
    print(f"  Fullname: {info['Name']}")
    print(f"  Address: {info['Address']}")
    print(f"  SSN: {info['SSN']}")
    print('  COURSES:')
    for courseid, grades in info['Courses'].items():
        print(f'    {courseid} - GPA = {calculate_gpa(grades)}')
        for assignment, grade in grades.items():
            print('           ', assignment, grade)
    print()
    

#print(calculate_gpa(students['mary20']['Courses']['T201FOR1'] ) )

#the_user = input('Username: ')
#while the_user != 'quit':
#    fullname = students[the_user]['Name']
#    address = students[the_user]['Address']
#    ssn = students[the_user]['SSN']

#    print(f'The user {the_user} name is {fullname}')
#    print(f'with ssn = {ssn} and lives at {address}')
#    the_user = input('Username: ')

###########Dæmi um forrit sem giskar á næsta orð út frá einhverjum texta. Fastinn TRAIL segir til um hversu mörg orð á að nota til að meta næsta orð.

import random
import string

EXPONENT = 1.5
TRAIL = 4

def clean_word(word):
    return word.strip(string.punctuation)    

def get_likely_next_word(words):
    total_count = sum([int(i**EXPONENT) for i in words.values()])
    threshold = random.randint(0,total_count)
    current_sum = 0
    for word, counts in words.items():
        current_sum += int(counts**EXPONENT)
        if current_sum >= threshold:
            return word
    return '.'


the_words = {}
#filename = 'shakespeare_all.txt'
filename = 'grimm.txt'
the_file = open(filename,'r')

last_words = []

for line in the_file:
    words = line.lower().split()
    for w in words:
        w = clean_word(w)
        if len(last_words) >= TRAIL:
            previous_last = tuple(last_words)

            if previous_last not in the_words:
                the_words[previous_last] = {}

            if w not in the_words[previous_last]:
                the_words[previous_last][w] = 0
            the_words[previous_last][w] += 1

        last_words.append(w)

        while len(last_words) > TRAIL:
            last_words.pop(0)


the_file.close()


sentence = input('Write: ').split()

for i in range(10):
    sentence.append( get_likely_next_word( the_words[ tuple(sentence[-TRAIL:])  ]))

print(' '.join(sentence))

