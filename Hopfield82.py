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

    def synchronousTesting(self, W, sPatterns):
        from numpy import vectorize, dot
        sgn = vectorize(lambda x: -1 if x < 0 else +1)
        oldPatterns = sPatterns
        while (True):
            sPatterns = sgn(dot(sPatterns, W))
            if (np.all(sPatterns == oldPatterns)):
                break
            oldPatterns = sPatterns
        return sPatterns

    def asynchronousTesting(self, W, asPatterns):
        from numpy import vectorize, dot
        import random
        sgn = vectorize(lambda x: -1 if x < 0 else +1)
        xPatterns = asPatterns
        yPatterns = asPatterns
        randomNumber = random.sample(range(0, len(yPatterns)), len(yPatterns))

        for x in range(0, len(randomNumber)):
            yPatterns[randomNumber[x]] = sgn(xPatterns[randomNumber[x]] + dot(yPatterns, W[:][randomNumber[x]]))
        return yPatterns

    def display(self,pattern):
        from pylab import imshow, cm, show
        imshow(pattern.reshape((50, 50)), cmap=cm.binary, interpolation='nearest')
        show()











