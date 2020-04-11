import random 
from matplotlib import pylab as plt

class drunkard():
    def __init__(self,name,x=0,y=0):
        self.name=name
        self.xpos=x 
        self.ypos=y 

    def getname(self):
        return self.name

    def take_step(self):
        deltax,deltay=random.choice([(0,1),(1,0),(-1,0),(0,-1)])
        
        self.xpos+=deltax
        self.ypos+=deltay
        return (self.xpos,self.ypos)

    def getPos(self):
        return (self.xpos,self.ypos)

class field():
    def __init__(self):
        self.drunkards={}
    
    def add_drunkard(self,drunkard):
        name=drunkard.getname()
        self.drunkards[name]=drunkard

    def show_all(self):
        print(self.drunkards)

    def everyone_walk(self,time):

                
        for men in self.drunkards:
            xs=[]
            ys=[]
            x,y=self.drunkards[men].getPos()
            xs.append(x)
            ys.append(y)

            for i in range(time):           
                x,y=self.drunkards[men].take_step()
                xs.append(x)
                ys.append(y)
            plt.figure()
            plt.title(men)
            plt.plot(xs,ys)

        #plt.show()


field=field()
for i in range(3):
    man=drunkard(str(i))
    field.add_drunkard(man)

field.show_all()
field.everyone_walk(100)



    