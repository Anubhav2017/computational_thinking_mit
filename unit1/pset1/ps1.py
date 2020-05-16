###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import copy
#================================
# Part A: Transporting Space Cows
#================================

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


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    sorted_cows=list(sorted(cows.items(),key=lambda item: item[1],reverse=True))
    #print(len(sorted_cows))
    trips=[]
    
    while len(sorted_cows)>0:
        curr_trip=[]
        avail=limit
        curr_cow=0
        
        while(curr_cow < len(sorted_cows)):
            #print(sorted_cows[curr_cow][0])
            if sorted_cows[curr_cow][1] <= avail:
                curr_trip.append(sorted_cows[curr_cow][0])
                avail-=sorted_cows[curr_cow][1]
            if avail==0:
                break
            curr_cow+=1
        for cow in curr_trip:
            sorted_cows.remove((cow,cows[cow]))    
        trips.append(curr_trip)

    return trips


# Problem 2
def val_of_trip(cows_list, trip):
    val=0
    for cow in trip:
        val+=cows_list[cow][1]

    return val

def smaller_fun(curr_list,curr_cow,limit,cows_list):
    if curr_cow ==len(cows_list):
        return
    
    store_additional=[]
    #print("lensol",len(curr_list))
    for sol in curr_list:
        can_add_into=[]
        i=0
        for trip in sol:
            value=val_of_trip(cows_list,trip)
            #print("value", value)
            if(value + cows_list[curr_cow][1]<= limit):
                
                can_add_into.append(i)
            i+=1
        #print("sol1",sol)    
        #print("cai",can_add_into)
        
        #additional_solns=[list(sol) for _ in range(len(can_add_into))]
        additional_solns=[copy.deepcopy(sol) for _ in range(len(can_add_into))]
        
            
        #print(len(can_add_into))
        #print("sol2",sol)
        #print("addsol0",additional_solns)
        for i in range(len(additional_solns)):
            additional_solns[i][can_add_into[i]].append(curr_cow)
        #print("sol3",sol)
        #print("addsol1",additional_solns)
         
        sol.append([curr_cow])
        #print("sol4",sol)
        
        #print("addsol2",additional_solns)
        store_additional+=additional_solns
    curr_list+=store_additional
    #print(curr_list)


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #print(list(cows.items()))
    cows_list=list(cows.items())
    curr_list=[[[0]]]
    for i in range(1,len(cows_list)):
        smaller_fun(curr_list,i,limit,cows_list)

    ans =sorted(curr_list,key=lambda x:len(x))[0]
    #print(ans)
    ansfinal=[]
    for item in ans:
        trip=[]
        for i in range(len(item)):
            trip.append(cows_list[item[i]][0])
        ansfinal.append(trip)
    return ansfinal


        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    s1=time.time()
    ans1=greedy_cow_transport(cows)
    e1=time.time()
    print("greedy time ",e1-s1)
    print(len(ans1))
    s2=time.time()
    ans2=brute_force_cow_transport(cows)
    e2=time.time()
    print("brute time ",e2-s2)
    print(len(ans2))


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

# cows = load_cows("ps1_cow_data.txt")
# limit=100
# print(cows)

# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
compare_cow_transport_algorithms()

