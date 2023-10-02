# Author: Tomas bragi Þorvaldsson, Bjarki Bjornsson, Larus Bergmann
# Date: 3/7/2023
# Project: Project3
# Acknowledgements: byggt eitthvað á fyrirlestrardæmum, geeks4geeks og stackoverflow hjálpaði einnig, codebeutify.org formattaði koðamm

import math

# main function
def main():
    filename = input("Distances: ")
    file_object = open_file(filename)
    if file_object is None:
        print("Invalid filename")
        return
    distances = get_distances(file_object)
    total_distance = greedy_distance(distances)
    improved_distance = improve_total_distance(distances, total_distance)
    print("Improved distance:", improved_distance)


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


# opens the file
def open_file(filename):
    try:
        file_object = open(filename, "r")
    except FileNotFoundError:
        return None
    else:
        return file_object


# puts distances in a list
def get_distances(file_obj):
    distances = []
    for line in file_obj:
        row = list(map(float, line.strip().split()))
        distances.append(row)
    return distances


# Find the closest neighbor for each unvisited location and makes a route using the greedy aproach
def greedy_distance(distances):
    n = len(distances)
    current_location = 0
    visited_locations = [current_location]
    unvisited_locations = list(range(1, n))
    total_distance = 0

    while unvisited_locations:
        closest_location = find_closest_neighbor(
            current_location, unvisited_locations, distances
        )
        visited_locations.append(closest_location)
        unvisited_locations.remove(closest_location)
        total_distance += distances[current_location][closest_location]
        current_location = closest_location

    total_distance += distances[current_location][0]

    print(f"Greedy distance: {total_distance}")


# Improves the greedy route
def improve_total_distance(distances, total_distance):
    n = len(distances)
    improved = True
    total_route = list(range(n))
    while improved:
        improved = False
        for i in range(n - 2):
            for j in range(i + 2, n):
                if j == n - 1 and i == 0:
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
                    total_route[i + 1 : j + 1] = reversed(total_route[i + 1 : j + 1])
                    improved = True
        total_distance = final_distance(distances, total_route)
    return total_distance


# calculates the total distance
def final_distance(distances, total_route):
    distance = 0
    for i in range(len(total_route)):
        distance += distances[total_route[i]][total_route[(i + 1) % len(total_route)]]
    return distance


if __name__ == "__main__":
    main()
