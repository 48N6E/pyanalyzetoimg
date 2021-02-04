import random
import matplotlib.pyplot as plt

class linechart:
    def __init__(self):
        self.x = random.randint(1,6)
        self.y = random.randint(10,11)


    def showlinechart(self):
        x = []
        y = []
        for i in range(10):
            x.append(random.randint(1, 6))
            y.append(random.randint(2, 6))
            print(x,y)
        print(self.x,self.y)
        plt.plot(x,y)
        plt.show()