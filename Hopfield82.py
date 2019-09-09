import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm


class Hopfield82:

    def create_weight_matrix(self, M):
        """ Create a weigth matrix
            input M: is a paterns matrix where each row is an input
            output w: weight matrix trained
        """
        if M.shape[0] is None:
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
        # is divided for the number of paterns instead N:neurons
        return c * 1 / M.shape[0]


    def energy(self, s, weigth_matrix, threshold):
        return -0.5 * s @ weigth_matrix @ s + np.sum(s * threshold)

    def update(self, s, weigth_matrix, num_iter, threshold, asyc) :
        if asyc != True or asyc != False:
            asyc == False
        elif asyc == True:
            #Asyn UPDATE
            #Initial energy state
            init_s = s;
            e = self.energy(init_s, weigth_matrix,threshold)
            for i in range(num_iter):
                for j in range(50):
                    # Select random neuron
                    idx = np.random.randint(0, weigth_matrix.shape[0] )

                    # Update s
                    init_s[idx] = np.sign(weigth_matrix[idx].T @ init_s - threshold)

                # Compute new state energy
                e_new = self.energy(init_s, weigth_matrix,threshold)

                # s is converged
                if e == e_new:
                    return init_s
                # Update energy
                e = e_new
        else:
            init_s = s

            e = self.energy(init_s, weigth_matrix,threshold)

            # Iteration
            for i in range(num_iter):
                # Update s
                init_s = np.sign(weigth_matrix@ init_s- threshold)
                # Compute new state energy
                e_new = self.energy(init_s, weigth_matrix,threshold)

                # s is converged
                if e == e_new:
                    return init_s
                # Update energy
                e = e_new
            return init_s







