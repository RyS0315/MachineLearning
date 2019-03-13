from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.manifold import Isomap
from sklearn.manifold import SpectralEmbedding

import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
import makeSemiCircles

def pltPer(X, y, W, it):
    f = plt.figure()
    if X.shape[1] > 3:
        # reduce dimensions for display purposes
        Xw = np.append(X, np.reshape(W, (1, len(W))), 0)   # add a column of ones
        #Xs = TSNE(n_components=2, random_state=0, verbose=1).fit_transform(Xw)
        #Xs = Isomap(n_components=2).fit_transform(Xw)
        Xs = SpectralEmbedding(n_components=2).fit_transform(Xw)
        #Xs = PCA(n_components=2, random_state=0).fit_transform(Xw)

        Xs = np.append(np.ones((Xs.shape[0],1)), Xs, 1)   # add a column of ones
        X = Xs[:-1,:]
        W = Xs[-1,:]
        #print(W.shape)
        
    for n in range(len(y)):
        if y[n] == -1:
            plt.plot(X[n,1],X[n,2],'r*')
        else:
            plt.plot(X[n,1],X[n,2],'b.')
    m, b = -W[1]/W[2], -W[0]/W[2]
    l = np.linspace(min(X[:,1]),max(X[:,1]))
    plt.plot(l, m*l+b, 'k-')
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.title("Perceptron Learning Algorithm Iteration: " + str(it))
    f.show()
    

def classification_error(w, X, y):
    err_cnt = 0
    N = len(X)
    for n in range(N):
        s = np.sign(w.T.dot(X[n])) # if this is zero, then :(
        if y[n] != s:
            err_cnt += 1
    print(err_cnt)
    return err_cnt

def choose_miscl_point(w, X, y):
    mispts = []
    # Choose a random point among the misclassified
    for n in range(len(X)):
        if np.sign(w.T.dot(X[n])) != y[n]:
            mispts.append((X[n], y[n]))
    #print(len(mispts))
    return mispts[random.randrange(0,len(mispts))]

def main():
    itlst = []
    for x in range(1):
        N = 2000

        # data    
        X, y = makeSemiCircles.make_semi_circles(n_samples=N, thk=25, sep=.1, rad=10)
        y[y==0] = -1  # replace the zeros    
        X = np.append(np.ones((N,1)), X, 1)   # add a column of ones

        #linear Regression
        Xs = np.linalg.pinv(X.T.dot(X)).dot(X.T)
        wlr = Xs.dot(y)
        pltPer(X,y,wlr, 0)
        # initialize the weigths to the linear regression 
        w = wlr
        it = 0

        bestW = w
        bestE = N
        nerr = classification_error(w, X, y)
        # Iterate until all points are correctly classified
        while nerr != 0:
            it += 1
            # Pick random misclassified point
            x, s = choose_miscl_point(w, X, y)
            # Update weights
            w += s*x
            nerr = classification_error(w, X, y)
            if nerr < bestE:
                bestE = nerr
                bestW = w
                bestIt = it
            elif (it - bestIt) > 25:
                print("Early Stop! No solution Found")
                break
        w = bestW
        pltPer(X,y,w, bestIt)
        print("Best Error = " + str(bestE) + " On iteration " + str(bestIt))
        print("Total iterations: " + str(it))
        itlst.append(it)
    print(itlst)
    f = plt.figure()
    plt.hist(itlst)
    plt.show()

main()