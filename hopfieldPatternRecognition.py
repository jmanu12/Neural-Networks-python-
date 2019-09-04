import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm

#The imput vectors are the paterns P1, P2
E1 = np.array([1,1,-1,-1])
E2 = np.array([-1, -1, 1, 1])
##############LEARNING######################3

def create_WeigthMatrix(x):
    if len(x.shape) != 1:
        print ("The input is not vector")
        return
    else:
        w = np.zeros([len(x),len(x)])
        for i in range(len(x)):
            for j in range(i,len(x)):
                if i == j:
                    w[i,j] = 0
                else:
                    w[i,j] = x[i]*x[j]
                    w[j,i] = w[i,j]
    print(w)
    return w
    #https://github.com/yosukekatada/Hopfield_network/blob/master/hopfield.py
create_WeigthMatrix(E2)