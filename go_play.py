import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
from utils import linechart,columndiagram


# x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
#
# plt.plot(x, y)
# plt.show()

if __name__ == '__main__':
    #折线图
    #test = linechart.linechart()
    #test.showlinechart()
    #直方图
    test = columndiagram.columndiagram()
    #test.showColumnDiagram()
    test.seabornColumnDiagram()
