import numpy as np
import matplotlib.pyplot as plt
# import pla

def pltPer(X, Y, W, title):
    f = plt.figure()
    for n in range(len(Y)):
        if Y[n] == -1:
            plt.plot(X[n,1],X[n,2],'r*')
        else:
            plt.plot(X[n,1],X[n,2],'b.')
    m, b = -W[1]/W[2], -W[0]/W[2]
    l = np.linspace(min(X[:,1]), max(X[:,1]))
    plt.plot(l, m*l+b, 'k-')
    f.show()
    plt.title(title)
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")

# #x0x1x2
# X = np.array(([[1,2,4],
#                [1,5,3],
#                [1,1,6],
#                [1,0,7]]))
# Y = np.array([1,1,-1,-1])
# W = np.array([2.3,3.2,0.1]) #w0w1w2
# pltPer(X,Y,W)

