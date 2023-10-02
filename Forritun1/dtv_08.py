number_of_numbers = int(input())

the_numbers = [False for _ in range(201)]
for i in range(number_of_numbers):
    the_numbers[ int(input()) ] = True

recited_numbers = 0
current_number = 1
all_correct = True

while recited_numbers < number_of_numbers:
    if the_numbers[current_number]:
        recited_numbers += 1
    else:
        print(current_number)
        all_correct = False
    current_number += 1

if all_correct:
    print('good job')

##############################


def find_the_odd_guest_list(invitations):
    for i,code in enumerate(invitations):
        if code > 0:
            odd_guest = True
            for j in range(i+1, len(invitations)):
                if invitations[j] == code:
                    invitations[i] = invitations[j] = -1
                    odd_guest = False
                    break
            if odd_guest:
                return code
    return -1

def find_the_odd_guest_dict(invitations):
    guests = {}
    for invite in invitations:
        if invite in guests.keys():
            guests[invite] += 1
        else:
            guests[invite] = 1

    for code, nr_of_guests in guests.items():
        if nr_of_guests == 1:
            return code
    return -1


cases = int(input())

nr_guests = []
invitations = []

for i in range(cases):
    nr_guests.append(int(input()))
    invitations.append([int(x) for x in input().split()])

for case in range(cases):
    code = find_the_odd_guest_dict(invitations[case])
    print(f'Case #{case+1}: {code}')

