import sys
import numpy
import scipy
import sklearn
import matplotlib
import pandas

class Problem3():
    def __init__(self):
        self.A = numpy.matrix([[1,4,-3], [2,-1,3]])
        self.B = numpy.matrix([[-2,0,5], [0,-1,4]])
        self.C = numpy.matrix([[1,0], [0,2]])
    def outputa(self):
        print(numpy.matmul(self.A, self.B))
    def outputb(self):
        print(numpy.linalg.matrix_rank(numpy.matmul(self.A.T, self.B)))
    def outputc(self):
        bt = self.B.T
        print(numpy.matmul(self.A, bt) + self.C.I)
p3 = Problem3()
# p3.outputa()
# p3.outputb()
p3.outputc()
