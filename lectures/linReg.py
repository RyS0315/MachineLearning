import random
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1,32)
y = []

Xs = np.linalg.pinv(X.T.dot(X)).dot(X.T)
w = Xs.dot(y)