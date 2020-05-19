def solveit(test):

    i=0

    while(True):

        if test(i):
            return i 
        if test(-i):
            return -i 
        i+=1