
def sorted_list( inputset ):
    set_as_list = list( inputset )
    set_as_list.sort()
    return set_as_list

sentence1 = input('First sentence: ')
sentence2 = input('Second sentence: ')

set1 = set(sentence1)
set2 = set(sentence2)

print('Common letters:', sorted_list( set1 & set2 ))
print('Only first:', sorted_list( set1 - set2 ))
print('Only second:', sorted_list( set2 - set1 ))

######################

QUIT = "q"
trans_dict = {}
sks = input("skammstofun: ")
while sks != QUIT:
    abbrev, translation = sks.split(',')
    trans_dict[abbrev] = translation.strip()
    sks = input("skamstofun: ")
print(trans_dict)

sent = input("sentence: ")
sentwords = sent.split(" ")

for i, word in enumerate(sentwords):
    if word in trans_dict:
        sentwords[i] = trans_dict[word]

new_sent = " ".join(sentwords)
print(new_sent)

#####################################

import string

def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

def build_dict(file_stream):
    ''' Extracts abbreviations and their corresponding English phrases from 
        a file stream, builds and returns a translation dictionar '''
    trans_dict = {}
    for line in file_stream:
        abbrev, translation = line.split(':')
        trans_dict[abbrev] = translation.strip()
    return trans_dict

def translate_abbrev(abbrev, translate_dict):
    ''' Returns a translation of a single abbreviation
        If the abbrevation ends with a punctuation mark, it remains a part of the translation '''
    last_char = abbrev[-1]
    if last_char in string.punctuation:
        abbrev = abbrev[:-1]
    else:
        last_char = ''
    
    if abbrev in translate_dict:
        word = translate_dict[abbrev]
    else:
        word = abbrev
    
    return word + last_char

def translate_message(message, translation_dict):
    ''' Returns a translation of a single message, consisting of a sequence of abbreviations '''
    translation = ''
    the_parts = message.split()

    for abbrev in the_parts:
        translation += translate_abbrev(abbrev, translation_dict) + " "

    return translation

def translate(translate_dict):
    message = input("Enter a message: ")
    while message != 'q':
        translation = translate_message(message, translate_dict)
        print(translation)
        message = input("Enter a message: ")


mapping_file = input("Enter name of mapping file: ")
file_stream = open_file(mapping_file)
if file_stream:
    translation_dict = build_dict(file_stream)
    file_stream.close()
    translate(translation_dict)

###############################

import csv

input_file = open('travel_log.csv', encoding='utf-8')
input_dict_reader = csv.DictReader( input_file, delimiter=',' )

travellers = {}

for line in input_dict_reader:
    name = line['Traveller']
    planet_from = line['Start']
    planet_to = line['Destination']
    if name not in travellers:
        travellers[name] = set()
    travellers[name].add( planet_from )
    travellers[name].add( planet_to )

input_file.close()

user_input = input('Write two names seperated with a comma (or quit): ')
while user_input != 'quit':
    person1, person2 = user_input.split(',')
    person1 = person1.strip()
    person2 = person2.strip()

    if person1 in travellers and person2 in travellers:
        print('{}: {} planets'.format(person1, len(travellers[person1])))
        print('{}: {} planets'.format(person2, len(travellers[person2])))
        print('{} planets in common.'.format( len(travellers[person1] & travellers[person2]) ))
    else:
        print('Person not found')

    user_input = input('Write two names seperated with a comma (or quit): ')