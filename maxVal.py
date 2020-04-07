import numpy as np 

class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildLargeMenu(numitems,maxVal,maxCost):
    menu=[]
    for i in range(numitems):
        menu.append(Food(str(i),np.random.randint(1,maxVal),np.random.randint(1,maxCost)))
    return menu 


def fastMaxVal(toConsider, avail,memo={}):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total weight of a solution to the
         0/1 knapsack problem and the items of that solution"""
    if (len(toConsider),avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        #Explore right branch only
        
        result=fastMaxVal(toConsider[1:],avail,memo)
        #memo[(len(toConsider[1:]), avail)]=result

    else:
        nextItem = toConsider[0]
        #Explore left branch
        #withVal, withToTake = memo[(len(toConsider[1:]), avail - nextItem.getCost())]
        withVal, withToTake = fastMaxVal(toConsider[1:],avail - nextItem.getCost(),memo)
        withVal += nextItem.getValue()
            
        #Explore right branch
        
        #withoutVal, withoutToTake = memo[(len(toConsider[1:]), avail)]
    
        withoutVal, withoutToTake = fastMaxVal(toConsider[1:],avail,memo)
        #memo[(len(toConsider[1:]), avail)]=(withoutVal,withoutToTake)


        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[((len(toConsider), avail))]=result
    return result