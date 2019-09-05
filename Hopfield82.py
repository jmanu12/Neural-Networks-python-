import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm


class Hopfield82:
    def create_weight_matrix(self, M):
        """ Create a weigth matrix
            input M: is a paterns matrix where each row is an input
            output w: weight matrix trained
        """
        if M.shape[0] < 1 or M.shape[0] == None:
            print("Error")
            return
        else:
            c = 0
            for p in range(M.shape[0]):
                x = M.A[p]
                w = np.zeros([len(x), len(x)])
                for i in range(len(x)):
                    for j in range(i, len(x)):
                        if i == j:
                            w[i, j] = 0
                        else:
                            w[i, j] = x[i] * x[j]
                            # by symmetry
                            w[j, i] = w[i, j]
                c = c + w
                print(c)
        # is divided for the number of paterns
        return c * 1 / M.shape[0]
