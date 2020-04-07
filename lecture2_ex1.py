import numpy as np 
import numpy.random as random
class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

def buildRandomItems(n):
    return [Item(str(i),10*random.randint(1,10),random.randint(1,10))
            for i in range(n)]

def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    bags=[]
    # enumerate the 2**N possible combinations
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 3 == 0:
                bag1.append(items[j])
            elif (i >> j)%3 == 1:
                bag2.append(items[j])
        bags.append((bag1, bag2))
        #yield bags
    return bags 


if __name__ == "__main__":
    items=['apple', 'orange', 'banana', 'grapes']
    items=buildItems()
    

    bags=yieldAllCombos(items)
    print([bag[0] for bag in bags])
    # for i in range(len(bags)):
    #     bag1, bag2=bags[i]
    #     print("1",bag1)
    #     print("2",bag2)
    #print(bag2)