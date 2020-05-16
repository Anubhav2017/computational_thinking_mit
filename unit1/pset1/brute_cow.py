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

def test_comb(cows,limit,curr_cow,avail):
    
    if(curr_cow==len(cows) or avail==0):
        #print(curr_cow, " decision0")
        return []
    elif(cows[curr_cow][1]>avail):
        #print(curr_cow," decision1")                
        result= test_comb(cows,limit,curr_cow+1,avail)
        #print(result)
        return result
    else:
        #print(curr_cow," decision2")
        curr_cow_weight=cows[curr_cow][1]
        curr_cow_name=cows[curr_cow][0]
        withcow_combs=test_comb(cows,limit,curr_cow+1,avail-curr_cow_weight)            

        for item in withcow_combs:
            item.append(curr_cow_name)
        
        #if len(withcow_combs)==0:
        withcow_combs.append([curr_cow_name])
        
        #print("currcow",curr_cow," with", withcow_combs)

        withoutcow_combs=test_comb(cows,limit,curr_cow+1,avail)
        #print("currcow",curr_cow," without", withoutcow_combs)
        ans=withcow_combs+withoutcow_combs        
        #print(ans)
        
        return ans



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
    cows_list=list(cows.items())
    ans=sorted(test_comb(cows_list,limit,0,limit),key=lambda x:len(x))
    return ans


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

    ans =sorted(curr_list,key=lambda x:len(x))
    print(ans)
    ansfinal=[]
    for item in ans:
        trip=[]
        for i in range(len(item)):
            trip.append(cows_list[item[i]][0])
        ansfinal.append(trip)
    return ansfinal
    

cows={'Miss Bella': 25, 'Lotus': 40, 'MooMoo': 50, 'Milkshake': 40, 'Horns': 25, 'Boo': 20}
print(brute_force_cow_transport(cows,45))

