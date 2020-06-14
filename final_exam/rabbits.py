import random
import matplotlib.pyplot as plt
import numpy as np
# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP


    prob_reproduction = 1- float(CURRENTRABBITPOP) / float(MAXRABBITPOP)

    incr=0
    for _ in range(CURRENTRABBITPOP):

      num=random.random()
      if( num< prob_reproduction):
        incr+=1

    if CURRENTRABBITPOP+incr > MAXRABBITPOP:
      CURRENTRABBITPOP=MAXRABBITPOP
    else:
      CURRENTRABBITPOP+=incr
  
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    if CURRENTFOXPOP < 10:
      return

    incfox=0
    decrabbit=0

  
    if CURRENTRABBITPOP > 10:

      for _ in range(CURRENTFOXPOP):
        num1=random.random()
        probeat= float(CURRENTRABBITPOP)/float(MAXRABBITPOP)

        if num1 < probeat:

          decrabbit +=1
          num2= random.random()
        
          if num2 < 0.3333333:
            incfox +=1

        else:

          for _ in range(CURRENTFOXPOP):
            if CURRENTFOXPOP > 10:
              num3=random.random()
              if num3 < 0.1:
                incfox -=1
    
    else:
      if CURRENTFOXPOP > 10:
        num3=random.random()
        if num3 < 0.1:
          incfox -=1

    if CURRENTFOXPOP + incfox > 10:
      CURRENTFOXPOP+=incfox
    
    
    if CURRENTRABBITPOP-decrabbit <10:
      CURRENTRABBITPOP = 10
    else:
      CURRENTRABBITPOP-= decrabbit


      
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_populations=[]
    fox_populations = []
    for t in range(numSteps):
      rabbitGrowth()
      foxGrowth()
      rabbit_populations.append(CURRENTRABBITPOP)
      fox_populations.append(CURRENTFOXPOP)
    
    return (rabbit_populations, fox_populations)



# foxGrowth()
# print(CURRENTFOXPOP)
# print(CURRENTRABBITPOP)
# foxGrowth()
# print(CURRENTFOXPOP)
# print(CURRENTRABBITPOP)

rabbit_populations, fox_populations=runSimulation(200)
print(rabbit_populations)
print(fox_populations)
coeffrabbit = np.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
plt.plot(np.polyval(coeffrabbit, range(len(rabbit_populations))))
plt.legend('rabbit')

coefffox = np.polyfit(range(len(fox_populations)), fox_populations, 2)
plt.plot(np.polyval(coefffox, range(len(fox_populations))))
plt.legend('fox')

plt.show()