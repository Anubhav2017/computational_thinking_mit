import copy

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict





cows=load_cows("ps1_cow_data.txt")

print(brute_force_cow_transport({'Miss Bella': 25, 'Lotus': 40, 'MooMoo': 50, 'Milkshake': 40, 'Horns': 25, 'Boo': 20}, 100))
#combs=sorted(combs,key=lambda x:len(x))
#ans=combs[0]