# Author: Eyjolfur Ingi Asgeirsson
# Date: 2023-02-26
# Project: T201FOR1 Project03
# Acknowledgements: remake of an old c++ problem from T208FOR2

def open_file(filename):
    try:
        distances_file = open(distances_filename, 'r')
        return distances_file
    except FileNotFoundError:
        print('Invalid filename')
        return None


def get_distances(distances_file):
    distances_raw = distances_file.readlines()

    nr_cities = len(distances_raw)
    distances = [[0 for _ in range(nr_cities)] for _ in range(nr_cities)]

    for i, line in enumerate(distances_raw):
        for j, distance in enumerate(line.split()):
            distances[i][j] = float(distance)

    return distances

def calculate_distance(distances, tour):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distances[tour[i-1]][tour[i]]
    return total_distance

def find_greedy_tour(distances, startcity = 0):
    current_city = startcity
    tour = [current_city,]
    nr_cities = len(distances)

    while len(tour) < nr_cities:
        shortest_distance = -1
        closest_city = -1
        for next_city in range(nr_cities):
            if (next_city not in tour) and (distances[current_city][next_city] < shortest_distance or shortest_distance < 0):
                shortest_distance = distances[current_city][next_city]
                closest_city = next_city
        tour.append(closest_city)
        current_city = closest_city

    return tour, calculate_distance(distances, tour)

def improve_tour(d, tour):
    t = tour.copy()
    nr_cities = len(tour)
    improvements_made = True

    while improvements_made:
        improvements_made = False
        for i in range(nr_cities):
            for j in range(i+1, nr_cities-1):
                if d[t[i-1]][t[i]] + d[t[j]][t[j+1]] > d[t[i-1]][t[j]] + d[t[j+1]][t[i]]:
                    #print(f'Improved, swapped ({t[i-1]},{t[i]}) and ({t[j]},{t[j+1]})')
                    #print(f'Previous distance: {calculate_distance(d, t)}')

                    subtour = t[i:j+1]
                    subtour.reverse()
                    t[i:j+1] = subtour
                    improvements_made = True

                    #print(f'Improved distance: {calculate_distance(d, t)}')

    return t, calculate_distance(d, t)


# ------------ Main part -----------------
distances_filename = input('Distances: ')

distances_file = open_file(distances_filename)

if distances_file:
    distances = get_distances(distances_file)
    distances_file.close()
    
    greedy_tour, greedy_distance = find_greedy_tour(distances, 0)

    improved_tour, improved_distance = improve_tour(distances, greedy_tour)
    
    # Print the solution to a file
    #solution_file = open('solution_greedy.txt', 'w')
    #for city in greedy_tour:
    #    print(city, file=solution_file)
    #solution_file.close()

    #solution_file = open('solution_improved.txt', 'w')
    #for city in improved_tour:
    #    print(city, file=solution_file)
    #solution_file.close()
    
    print(f'Greedy distance: {greedy_distance}')
    print(f'Improved distance: {improved_distance}')