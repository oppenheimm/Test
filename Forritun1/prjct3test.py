import math


def open_the_file(filename):
    distance_matrix = []
    try:
        with open(filename) as f:
            for line in f:
                row = [float(x) for x in line.split()]
                distance_matrix.append(row)
    except FileNotFoundError:
        print("Invalid filename")
        exit()
    return distance_matrix

#finds route by constantly going to the nearest location
def find_greedy_route(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    route = [0]
    visited[0] = True
    for i in range(1, n):
        min_distance = float("inf")
        next_location = None
        current_location = route[-1]
        for j in range(n):
            if not visited[j] and distance_matrix[current_location][j] < min_distance:
                min_distance = distance_matrix[current_location][j]
                next_location = j
        visited[next_location] = True
        route.append(next_location)
    route.append(0)
    return route

#improves the route
def improve_route(distance_matrix, route):
    n = len(distance_matrix)
    improved = True
    while improved:
        improved = False
        for i in range(n):
            for j in range(i + 2, n):
                if j == n - 1 and i == 0:
                    continue
                distance1 = (
                    distance_matrix[route[i]][route[i + 1]]
                    + distance_matrix[route[j]][route[j + 1]]
                )
                distance2 = (
                    distance_matrix[route[i]][route[j]]
                    + distance_matrix[route[i + 1]][route[j + 1]]
                )
                if distance1 > distance2:
                    route[i + 1 : j + 1] = reversed(route[i + 1 : j + 1])
                    improved = True
    return route


# calculates the total distance
def total_distance(distance_matrix, route):
    distance = 0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i]][route[i + 1]]
    return distance



filename = input("Enter filename: ")

distance_matrix = open_the_file(filename)
greedy_route = find_greedy_route(distance_matrix)
greedy_distance = total_distance(distance_matrix, greedy_route)
print("Greedy route distance:", greedy_distance)

improved_route = improve_route(distance_matrix, greedy_route)
improved_distance = total_distance(distance_matrix, improved_route)
print(improved_distance)