# Author: <Tomas bragi thorvaldsson>
# Date: <21/4/2023>
# Project: <final_03>

d = {}
team_goals = {}
points = {}

WIN = 3
EVEN = 1


def total_points(f):
    # this function calculates total points
    for line in f:
        (teams, points) = line.split(" ")
        (team1, team2) = teams.split("-")
        (point1, point2) = points.split("-")
        d[(team1)] = int(point1)
        d[(team2)] = int(point2)

        if team1 not in points:
            points[team1] = {"point": 0}
        if int(point1) > int(point2):
            points[team1]["point"] += 3
        if int(point1) == int(point2):
            points[team1]["point"] += 1

        if team2 == team1:
            points[team2] = {"point": 0}
        if int(point2) > int(point1):
            points[team2]["point"] += int(WIN)
        if int(point1) == int(point2):
            points[team2]["point"] += int(EVEN)


def total_goals(f):
    # this function calculates total goals
    for line in f:
        (teams, points) = line.split(" ")
        (team1, team2) = teams.split("-")
        (point1, point2) = points.split("-")
        d[(team1)] = int(point1)
        d[(team2)] = int(point2)

        if team1 not in team_goals:
            team_goals[team1] = {"total_goals": 0}

            team_goals[team1]["total_goals"] += int(point1)

            if team2 == team1:
                team_goals[team1] = {"total_goals": 0}

        team_goals[team1]["total_goals"] += int(point2)


filename = input("Filename: ")

try:
    input_file = open(filename, "r")

    total_points(input_file)

    input_file.close()


except FileNotFoundError:
    print("Invalid filename")

for team1, stats in sorted(points.items()):
    point = stats["point"]
    total_goals = stats["total_goals"]
    print(f"Name: {team1}, Total points: {points}, Total goals: {total_goals}")
