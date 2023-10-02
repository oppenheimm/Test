import random

# Define player and enemy attributes
player = {"name": "Player", "health": 100, "attack": 10, "defense": 5}
enemy = {"name": "Enemy", "health": 100, "attack": 8, "defense": 8}

# Define function for player attack
def player_attack():
    damage = player["attack"] - enemy["defense"]
    if damage < 0:
        damage = 0
    enemy["health"] -= damage
    print(f"{player['name']} attacked {enemy['name']} for {damage} damage.")

# Define function for enemy attack
def enemy_attack():
    damage = enemy["attack"] - player["defense"]
    if damage < 0:
        damage = 0
    player["health"] -= damage
    print(f"{enemy['name']} attacked {player['name']} for {damage} damage.")

# Define function to check if someone has won
def check_win():
    if player["health"] <= 0:
        print(f"{enemy['name']} wins!")
        return True
    elif enemy["health"] <= 0:
        print(f"{player['name']} wins!")
        return True
    else:
        return False

# Main game loop
while True:
    # Player turn
    player_attack()
    if check_win():
        break
    
    # Enemy turn
    enemy_attack()
    if check_win():
        break
