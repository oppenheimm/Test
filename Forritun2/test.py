import random

# Constants
grid_width = 40
grid_height = 25
total_trees = 1000
fire_prob_left = 0.8
fire_prob_right = fire_prob_above = fire_prob_below = 0.3
simulations = 10000  # Number of simulations
burnt_threshold = 0.30  # 30% threshold


def simulate_fire_spread():
    forest = [[0] * grid_width for _ in range(grid_height)]
    # Start the fire at the top-left corner
    forest[0][0] = 1
    burnt_count = 1  # Count the initially burnt tree

    while True:
        new_forest = [[0] * grid_width for _ in range(grid_height)]
        fire_spread = False

        for row in range(grid_height):
            for col in range(grid_width):
                if forest[row][col] == 1:
                    # Check neighbors and update probabilities
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        r, c = row + dr, col + dc
                        if 0 <= r < grid_height and 0 <= c < grid_width:
                            if new_forest[r][c] == 0:
                                # Probability of catching fire based on direction
                                if dc == 1:
                                    prob = fire_prob_left
                                else:
                                    prob = fire_prob_right
                                if dr == 1 or dr == -1:
                                    prob = fire_prob_above
                                # Check if the tree catches fire
                                if random.random() < prob:
                                    new_forest[r][c] = 1
                                    fire_spread = True
                                    burnt_count += 1

        forest = new_forest

        # Check if the fire has stopped spreading
        if not fire_spread:
            break

    return burnt_count / total_trees


# Perform simulations
count_more_than_threshold = 0
for _ in range(simulations):
    burnt_percentage = simulate_fire_spread()
    if burnt_percentage > burnt_threshold:
        count_more_than_threshold += 1

# Calculate the estimated probability
estimated_probability = count_more_than_threshold / simulations
print("Estimated Probability:", estimated_probability)
