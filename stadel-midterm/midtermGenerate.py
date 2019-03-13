import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
import plotP
# read digits data & split it into X (training input) and y (target output)
dataset = genfromtxt('features.csv', delimiter=' ')
y = dataset[:, 0]
X = dataset[:, 1:]
X = np.append(np.ones((X.shape[0],1)), X, 1)   # add a column of ones

y[y!=4] = -1    #rest of numbers are negative class
y[y==4] = +1    #number zero is the positive class
# plots data 
c0 = plt.scatter(X[y==-1,1], X[y==-1,2], s=20, color='r', marker='x')
c1 = plt.scatter(X[y==1,1], X[y==1,2], s=20, color='b', marker='o')
# displays legend
plt.legend((c0, c1), ('All Other Numbers -1', 'Number Zero +1'), 
        loc='upper right', scatterpoints=1, fontsize=11)
# displays axis legends and title
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.title(r'Intensity and Symmetry of Digits')

def pltPer(X, Y, W):
    if X.shape[1] > 3:
        #reduce dimensions for display purposes
        xw = np.append(X, np.reshape(W, (1,len(W))), 0)
        # xs = TSNE(n_components=2).fit_transform(xw)
        xs = PCA(n_components=2, random_state=0).fit_transform(X)
        xs = np.append(np.ones((xs.shape[0],1)), xs, 1)
        X = xs[:-1,:]
        W = xs[-1,:]
        # W = np.reshape((W.shape[1],))
        print("X- Shape" + str(xs.shape))

    m, b = -W[1]/W[2], -W[0]/W[2]
    l = np.linspace(min(X[:,1]), max(X[:,1]))
    plt.plot(l, m*l+b, 'k-')
    plt.xlabel("$X_1$")
    plt.ylabel("$X_2$")


############## Linear Regression ###################
# Xs = np.linalg.pinv(X.T.dot(X)).dot(X.T)
# wlr = Xs.dot(y)
# it = 0
# nerr = plotP.classification_error(wlr, X, y)
# print("Error" + str(nerr))
# print("Iteration" + str(it))
# pltPer(X, y, wlr)
# plt.savefig('midterm.plot-1b.pdf', bbox_inches='tight')
# plt.show()

# ############### Pocket Algorithm ###################
# w = np.zeros(3)
# it = 0

# bestW = w
# bestE = 7000
# nerr = plotP.classification_error(w, X, y)
# # Iterate until all points are correctly classified
# while nerr != 0:
#     it += 1
#     # Pick random misclassified point
#     x, s = plotP.choose_miscl_point(w, X, y)
#     # Update weights
#     w += s*x
#     nerr = plotP.classification_error(w, X, y)
#     if nerr < bestE:
#         bestE = nerr
#         bestW = w
#         bestIt = it
#     elif (it - bestIt) > 25:
#         print("Early Stop! No solution Found")
#         break
# w = bestW
# pltPer(X, y, w)
# print("Error " + str(bestE))
# print("Iteration " + str(bestIt))
# plt.savefig('midterm.plot-1a.pdf', bbox_inches='tight')
# plt.show()

# ###################### Pocket Algorithm Starting With Linear Regression ##################
Xs = np.linalg.pinv(X.T.dot(X)).dot(X.T)
wlr = Xs.dot(y)

w = wlr
it = 0

bestW = w
bestE = 7000
nerr = plotP.classification_error(w, X, y)
# Iterate until all points are correctly classified
while nerr != 0:
    it += 1
    # Pick random misclassified point
    x, s = plotP.choose_miscl_point(w, X, y)
    # Update weights
    w += s*x
    nerr = plotP.classification_error(w, X, y)
    if nerr < bestE:
        bestE = nerr
        bestW = w
        bestIt = it
    elif (it - bestIt) > 25:
        print("Early Stop! No solution Found")
        break
w = bestW
print("Error " + str(bestE))
print("Iteration " + str(bestIt))
pltPer(X, y, w)
plt.savefig('midterm.plot-1c.pdf', bbox_inches='tight')
plt.show()

