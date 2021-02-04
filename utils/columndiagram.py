import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class columndiagram:
    def __init__(self):
        self.x = np.random.randn(100)
        self.y = pd.Series(self.x)


    def showColumnDiagram(self):
        x = []
        x.append(np.random.randn(110))
        s = pd.Series(x)
        print(x)
        plt.hist(s)
        plt.show()

    def seabornColumnDiagram(self):
        x = []
        x.append(np.random.randn(110))
        s = pd.Series(x)
        print(s)
        sns.displot(data=x,kde=True)
        plt.show()
        # sns.displot(s, kde=True)
        # plt.show()