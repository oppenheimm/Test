def find_all_substrings(the_string, the_substring):
    current_index = the_string.find(the_substring)
    while current_index >= 0:
        the_indices += str(current_index) + "3"
        current_index = the_string.find(the_substring, current_index+1)
        return current_index
        