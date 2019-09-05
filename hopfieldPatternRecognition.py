import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm
from Hopfield82 import Hopfield82
#The imput vectors are the paterns P1, P2
M = np.matrix("1,1,-1,-1; -1,-1,1,1")
##############LEARNING######################
w = Hopfield82()
R = w.create_weight_matrix(M)
print('************************')
print(R)






    #https://github.com/yosukekatada/Hopfield_network/blob/master/hopfield.py
