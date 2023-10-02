number_of_players = int(input(""))

player_count = 0
contributions = 0
remainder = 0

while number_of_players < 2:
    number_of_players = int(input(""))

while player_count < number_of_players:
    contribute = int(input(""))
    contributions = contributions + contribute
    player_count += 1
remainder = remainder + (contributions % player_count)
print("The sum of all contributions is", contributions)
print(
    f"When {contributions} is divided by {number_of_players}, the remainder is {remainder}"
)
print("Player", remainder, "is the winner!")
