import numpy as np


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
    numcomb= 2**(len(choices))
    nums=[]
    sumresults=[]

    for i in range(numcomb):
        arr=np.asarray([int(x) for x in bin(i)[2:].zfill(len(choices))])
        
        num1=sum(arr*np.asarray(choices))
        
        nums.append(total-num1)
        sumresults.append(sum(arr))
    
    minimum=min([x for x in nums if x>=0])


    minindices= [i for i in range(len(nums)) if nums[i]==minimum]


    arrsums=[sumresults[i] for i in minindices]

    
    ind=minindices[arrsums.index(min(arrsums))]



    return np.asarray([int(x) for x in bin(ind)[2:].zfill(len(choices))])


print(find_combination([1, 81, 3, 102, 450, 10], 9))