def getIndex(num, choices):
    for i in range(len(choices)):
        if choices[i] == num:
            return i 

def doesExist(choices,total):
    if len(choices) == 0
    max=max(choices)





def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """

    while(True):
        maxnum=max(choices) 