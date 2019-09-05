import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm
class Hopfield82:
    def create_weight_matrix(self,x):
        """ Create a weigth matrix
            input x: is a vector of the patern
            output w: weight matrix
        """
        if len(x.shape) != 1:
            print("The input is not vector")
            return
        else:
            w = np.zeros([len(x), len(x)])
            for i in range(len(x)):
                for j in range(i, len(x)):
                    if i == j:
                        w[i, j] = 0
                    else:
                        w[i, j] = x[i] * x[j]
                        # by symmetry
                        w[j, i] = w[i, j]
        return w