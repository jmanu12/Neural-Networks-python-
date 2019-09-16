import numpy as np
from time import sleep
import sys

class HopfieldErrorEstimation:

    def weigthMatrix(self, paternMatrix):
        """
        :param paternMatrix: the matrix with the patterns
        :return: weigth matrix
        """
        print('CALCULATING THE WEIGTH MATRIX' + '\n')
        self.progress();
        print(paternMatrix.shape[0])
        W = 1 / (paternMatrix.shape[1]) * (
                    np.dot(paternMatrix, (np.transpose(paternMatrix))) - paternMatrix.shape[0] * np.identity(
                paternMatrix.shape[0], dtype=float))
        return W

    def generateRamdomPaterns(self, N, M):
        print('GENERATING RANDOM DATA'+ '\n')
        print('NUMBER OF BITS:' + '\n')
        print(N)
        print('NUMBER OF PATERNS:' + '\n')
        print(M)
        self.progress();
        """
        :param N: the number of bits for each pattern
        :param M: the number of patterns
        :return: a matrix with the patterns in each colummn generated as pseudo random
        """
        random_array = np.random.randint(2, size=(N, M))
        random_array = np.where(random_array == 0, -1, random_array)
        return random_array

    def updateSync(self, weigth_matrix, patern_matrix):
        """
        :param weigth_matrix: weith matrix
        :param patern_matrix: input matrix generated with the pseudo random paterns
        :return: the update matrix
        """
        print('UPDATING' + '\n')
        self.progress();
        update = np.dot(weigth_matrix, patern_matrix)
        update = np.where(update < 0, -1, update)
        update = np.where(update > 0, 1, update)
        return update

    def error(self, update_paterns, paterns):
        """
        :param update_paterns: update matrix with
        :param paterns: the input
        :return: the Error Probability = number of wrong bits/total bits
        """
        print('ERROR' + '\n')
        self.progress();
        v = (update_paterns == paterns)
        return list(v.flatten()).count(False) / (update_paterns.shape[0] * update_paterns.shape[1])

    def progress(self):
        for i in range(21):
            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
            sys.stdout.flush()
            sleep(0.25)
    def deleteConexions(self, weigth):
        value = np.array(weigth).flatten();
        randnums = np.random.randint(1, weigth.shape[0]*weigth.shape[0], 100)
        value[randnums] = 0
        return value.reshape(weigth.shape[1], weigth.shape[1])