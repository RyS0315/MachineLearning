import pla
import numpy as np
from sklearn.datasets.samples_generator import make_blobs
import pandas as pd
import matplotlib.pyplot as plt

#Parts A and B
def PartsAB():
    N = 20
    X,y = make_blobs(n_samples=N, centers=2, n_features=2 )
    y[y==0] = -1
    X = np.append(np.ones((N,1)),X, 1)
    w = np.zeros(3)

    pla.main(X, y, w, "1.4 Part A and B")

#Part C -> same as A but a different set of data
def PartC():
    N = 20
    X,y = make_blobs(n_samples=N, centers=2, n_features=2 )
    y[y==0] = -1
    X = np.append(np.ones((N,1)),X, 1)
    w = np.zeros(3)
    pla.main(X, y, w, "1.4 Part C" )

#Part D
def PartD():
    N = 100
    X,y = make_blobs(n_samples=N, centers=2, n_features=2 )
    y[y==0] = -1
    X = np.append(np.ones((N,1)),X, 1)
    w = np.zeros(3)

    pla.main(X, y, w, "1.4 Part D")

#Part E
def PartE():
    N = 1000
    X,y = make_blobs(n_samples=N, centers=2, n_features=2 )
    y[y==0] = -1
    X = np.append(np.ones((N,1)),X, 1)
    w = np.zeros(3)

    pla.main(X, y, w, "1.4 Part E")

#Part F
def PartF():
    N = 1000
    X,y = make_blobs(n_samples=N, centers=2, n_features=10 )
    y[y==0] = -1
    X = np.append(np.ones((N,1)),X, 1)
    w = np.zeros(11)

    pla.main(X, y, w, "1.4 Part F")

def PartG():
    histogram = Histogram()
    for i in range(0,100):
        N = 1000
        X,y = make_blobs(n_samples=N, centers=2, n_features=10 )
        y[y==0] = -1
        X = np.append(np.ones((N,1)),X, 1)
        w = np.zeros(11)
        itr = pla.main(X, y, w, "1.4 Part G")
        histogram.addPoints(itr)
    histogram.drawHistogram()

class Histogram():
    def __init__(self):
        self.points = []

    def addPoints(self, x):
        self.points.append(x)
    
    def getPoints(self):
        return self.points
    
    def drawHistogram(self):
        commutes = pd.Series(self.getPoints())

        commutes.plot.hist(grid=True, bins=20, rwidth=0.9,
                        color='#607c8e')
        plt.title('Converge iterations for random data')
        plt.xlabel('Iterations')
        plt.ylabel('Occurences')
        plt.grid(axis='y', alpha=0.75)
        plt.show()




# PartsAB()
# PartC()
# PartD()
# PartE()
# PartF()
PartG()

