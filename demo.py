import random

random.seed(9001)
d = random.randint(1, 10)#1
for i in range(random.randint(1, 10)):#5   5 2 10
    if random.randint(1, 10) < 7:
        print(d)
    else:
        random.seed(9001)
        d = random.randint(1, 10) #1
        print(random.randint(1, 10)) 