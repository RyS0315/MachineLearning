import math
def iterativeGenError(dvc, conf, gErr):
    N = 1000 #Initial Guess
    print("Initial N: " + str(N))
    it = 0
    while(N + ((1 - conf)*N) <= (8/gErr)*math.log((4*(2*math.pow(N, dvc))) / gErr, 2) ):
        it += 1
        N = (8/gErr)*math.log((4*(2*math.pow(N, dvc))) / gErr, 2)
        print("Iteration " + str(it) + " N: "+ str(N))

    print("Final N: " + str(N))
iterativeGenError(10, .95, .05)