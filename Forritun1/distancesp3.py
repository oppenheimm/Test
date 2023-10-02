import matplotlib.pyplot as plt
import math

# function finds the closest unvisited location to the current location
def find_closest_neighbor(current_location, unvisited_locations, distances):
    closest_location = unvisited_locations[0]
    closest_distance = math.inf
    for location in unvisited_locations:
        distance = distances[current_location][location]
        if distance < closest_distance:
            closest_distance = distance
            closest_location = location
    return closest_location

# Improve the route
def improve_total_distance(distances, total_distance):
    n = len(distances)
    improved = True
    total_route = list(range(n))
    while improved:
        improved = False
        for i in range(n-2):
            for j in range(i + 2, n):
                if j == n-1 and i == 0:
                    continue
                distance1 = (
                    distances[total_route[i]][total_route[i + 1]]
                    + distances[total_route[j]][total_route[(j + 1) % n]]
                )
                distance2 = (
                    distances[total_route[i]][total_route[j]]
                    + distances[total_route[i + 1]][total_route[(j + 1) % n]]
                )
                if distance1 > distance2:
                    total_route[i + 1:j + 1] = reversed(total_route[i + 1:j + 1])
                    improved = True
        total_distance = slime_distance(distances, total_route)
    return total_distance

# calculates the total distance
def slime_distance(distances, total_route):
    distance = 0
    for i in range(len(total_route)):
        distance += distances[total_route[i]][total_route[(i + 1) % len(total_route)]]
    return distance
# Load the distances data

filename = input("Enter filename: ")

distances = []
with open(filename) as f:
    for line in f:
        row = list(map(float, line.strip().split()))
        distances.append(row)

# Define the initial variables
n = len(distances)
current_location = 0
visited_locations = [current_location]
unvisited_locations = list(range(1, n))
total_distance = 0

# Find the closest neighbor for each unvisited location
while unvisited_locations:
    closest_location = find_closest_neighbor(current_location, unvisited_locations, distances)
    visited_locations.append(closest_location)
    unvisited_locations.remove(closest_location)
    total_distance += distances[current_location][closest_location]
    current_location = closest_location

# Add the distance from the last location back to the starting location
total_distance += distances[current_location][0]

print(total_distance)

# Improve the route and print the improved distance
improved_distance = improve_total_distance(distances, total_distance)
print("Improved distance:", improved_distance)
