import sys
import numpy as np
import scipy
import sklearn
import matplotlib
import matplotlib.pyplot as plt
import pandas

X = np.array(([[1,2,4],
               [1,5,3],
               [1,1,6],
               [1,0,7]]))
y = np.array([1,1,-1,-1])
W = np.array([2.3,3.2,0.1]) #w0w1w2


def pltPer(X,y,W):
    for n in range(len(y)):
        if(y[n] < 0):
            plt.plot(X[n,1], X[n,2], 'r.')
        else:
            plt.plot(X[n,1], X[n,2], 'b.')
    m, b = -W[1]/W[2], -W[0]/W[2]
    l = np.linspace(0,5)
    plt.plot(l, m*l+b, 'k-')

pltPer(X,y,W)
plt.show()