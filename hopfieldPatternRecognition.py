import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm
from Hopfield82 import Hopfield82
#The imput vectors are the paterns P1, P2
E1 = np.array([1,1,-1,-1])
E2 = np.array([-1, -1, 1, 1])
##############LEARNING######################
w = Hopfield82()
r = w.create_weight_matrix(E1)
print(r)

    #https://github.com/yosukekatada/Hopfield_network/blob/master/hopfield.py
