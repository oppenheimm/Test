player_1 = input("Player 1's move: ")
player_2 = input("Player 2's move: ")

player_1_input_ok = (player_1 == 'rock' or player_1 == 'scissors' or player_1 == 'paper')
player_2_input_ok = (player_2 == 'rock' or player_2 == 'scissors' or player_2 == 'paper')

if player_1_input_ok and player_2_input_ok:
    if (player_1 == 'rock' and player_2 == 'scissors') or (player_1 == 'scissors' and player_2 == 'paper') or (player_1 == 'paper' and player_2 == 'rock'):
        print('Winner: Player 1')
    elif (player_2 == 'rock' and player_1 == 'scissors') or (player_2 == 'scissors' and player_1 == 'paper') or (player_2 == 'paper' and player_1 == 'rock'):
        print('Winner: Player 2')
    else:
        print("It's a draw")
else:
    print('Wrong input')

###########################################################################################################################################################################################

the_max = -1
the_min = -1
counter = 0
the_sum = 0

first_iteration = True

current_input = input('Value: ')

while current_input != 'done':
    current_value = float(current_input)

    if the_max < current_value or first_iteration:
        the_max = current_value
    if the_min > current_value or first_iteration:
        the_min = current_value
    first_iteration = False

    counter += 1
    the_sum += current_value

    current_input = input('Value: ')

print('Max:', the_max)
print('Min:', the_min)
print('Mean:', the_sum / counter)