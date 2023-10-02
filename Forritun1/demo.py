def get_country_votes():

    country, votes = None, None

    input_file = input("Candidate and votes: ")
    country = input_file[1].lower()
    votes = int(input_file[2])
    
    return country, votes
    
    
def add_results(result_dict, country, votes):
    '''Adds the votes to the given to country in the given dictionar'''
    if country in result_dict:
        result_dict[country] += votes
    else:
        result_dict[country] = votes

def get_total_votes(result_dict):
    '''Returns the total number of votes for the given result dictionary'''
    total = 0
    for country in result_dict:
        total += result_dict[country]
    
    return total
    # Simpler solution
    # return sum(result_dict.values())


def print_results(result_dict):
    '''Prints the current results of the voting in ascending order country names'''
    for country in sorted(result_dict):
        print("{}: {}".format(country, result_dict[country]))

# Main    
voting_dict = {}
country = ''

while country is not None:
    country, votes = get_country_votes()
    if country is not None:
        if votes is not None:
            add_results(voting_dict, country, votes)
        else:
            print("Invalid no. of votes!")

print_results(voting_dict)
print("Total no. of votes: {}".format(get_total_votes(voting_dict)))



