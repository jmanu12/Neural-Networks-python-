from numpy import vectorize, dot
import random
from pylab import cm
from ImageIO import ImageIO
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
import sys

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
            # show progress bar
            print("LEARNING" + '\n')
            self.progress()
            for p in range(M.shape[0]):
                x = M.A[p]
                w = np.zeros([len(x), len(x)],dtype=np.float64)
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
        sgn = vectorize(lambda x: -1 if x < 0 else +1)
        oldPatterns = sPatterns

        fig, ax = plt.subplots(1, 1)
        im = ax.imshow(oldPatterns.reshape((50, 50)), cmap=cm.binary, interpolation='nearest')
        plt.axis('off')
        while (True):
            print("SYNC TESTING" + '\n')
            self.progress()
            sPatterns = sgn(dot(sPatterns, W))
            im.set_data((sPatterns.reshape((50, 50))))
            fig.canvas.draw_idle()
            plt.pause(0.0000000001)
            if (np.all(sPatterns == oldPatterns)):
                break
            oldPatterns = sPatterns

        return sPatterns

    def asynchronousTesting(self, W, asPatterns):
        new_data2 = ImageIO()
        sgn = vectorize(lambda x: -1 if x < 0 else +1)
        xPatterns = asPatterns
        yPatterns = asPatterns
        randomNumber = random.sample(range(0, len(yPatterns)), len(yPatterns))

        fig, ax = plt.subplots(1, 1)
        im = ax.imshow(yPatterns.reshape((50, 50)), cmap=cm.binary, interpolation='nearest')
        plt.axis('off')
        e = []
        # show progress bar
        print("ASYNC TESTING" + '\n')
        self.progress()
        for x in range(0, len(randomNumber)):
            yPatterns[randomNumber[x]] = sgn(xPatterns[randomNumber[x]] + dot(yPatterns, W[:][randomNumber[x]]))
            #energy
            e.append(-1 / 2 * np.dot((np.transpose(yPatterns)), dot(W, yPatterns)))

            #Learning with the update paterns
            im.set_data((yPatterns.reshape((50, 50))))
            fig.canvas.draw_idle()
            plt.pause(0.0000000000001)
        return yPatterns,e

    def energy(self, w, x):
        e = 0
        for i in range(0,2500):
            for j in range(0,2500):
                e += w[i][j] * x[i] * x[j]
        return e * (-0.5)

    def progress(self):
        for i in range(21):
            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
            sys.stdout.flush()
            sleep(0.25)


