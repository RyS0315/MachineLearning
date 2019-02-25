# Some attempt to do the PLA 

import numpy as np
import random
import PlotP
from sklearn.datasets.samples_generator import make_blobs
N = 1000
X,y = make_blobs(n_samples=N, centers=2, n_features=10 )
y[y==0] = -1
X = np.append(np.ones((N,1)),X, 1)

# print(X)
# print(y)
# N = len(X) # or X.shape[0]

def main(X, y):    
    # initialize the weigths to zeros
    w = np.zeros(11)
    it = 0
    
    # Iterate until all points are correctly classified
    while classification_error(w, X, y) != 0:
        it += 1
        # Pick random misclassified point
        x, s = choose_miscl_point(w, X, y)
        # Update weights
        w += s*x

        #if save:
        #    self.plot(vec=w)
        #    plt.title('N = %s, Iteration %s\n' \
        #              % (str(N),str(it)))
        #    plt.savefig('p_N%s_it%s' % (str(N),str(it)), \
        #                dpi=200, bbox_inches='tight')
    PlotP.pltPer(X,y,w, it)
    PlotP.plt.show()
    print("Total Iterations: " + str(it))

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
    print(len(mispts))
    return mispts[random.randrange(0,len(mispts))]

main(X,y)





