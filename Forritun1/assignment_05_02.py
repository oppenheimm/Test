# Author: <Tómas Bragi Þorvaldsson> 
# Date: <12.3.2023> 
# Project: <skilaverk 5 d 2> 
# Acknowledgements: ivar hannesson hjalpaði mer mikið með þennan koða og codebeutify formatter

def candidate_inputs():
    candidate_input = input("Candidate and votes: ")
    return candidate_input


candidates = {}

total = 0

USER_QUIT = ""

candidate_input = candidate_inputs()

while candidate_input != USER_QUIT:

    if USER_QUIT:
        break

    candidate_split = candidate_input.split()

    invalid_input = False

    if len(candidate_split) < 2 or not (candidate_split[1].isdigit() if len(candidate_split) > 1 else True):
        if not invalid_input:
            print("Invalid input!")
            invalid_input = True
        continue

    try:
        nr_vote = int(candidate_split[1])

        if nr_vote < 0:
            if not invalid_input:
                print("Invalid no. of votes!")
                invalid_input = True
            continue

        name = candidate_split[0].lower()

        candidates[name] = candidates.get(name, 0) + nr_vote

        total += nr_vote
    except ValueError:
        if not invalid_input:
            print("Invalid number of votes!")
            invalid_input = True

    candidate_input = candidate_inputs()

for name, votes in sorted(candidates.items()):
    print(f"{name}: {votes}")
print(f"Total no. of votes: {total}")

