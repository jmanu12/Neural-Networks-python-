import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

class SimplePerceptron:
    """
    Classifier: one layer perceptron
    """
    def __init__(self, eta = 0.1,  n_iter = 10  ):
        self.eta = eta
        self.n_iter = n_iter
    def fit_weights(self, X, y):
        """
        Fit the train data
        :param X:
        :param y:
        :return: selt object
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self


    def predict(self, X):
        """
        RETURNS 1 OR -1 DEPENDING OF THE ACTIVATION FUCTION
        :param X:
        :return: 1 OR -1
        """
        phi = np.where(self.net_input(X) >= 0.0, 1, -1)
        return phi

    def net_input(self, X):
        """
        Calculates the value of the activation  fuction
        #Z = W . X + theta
        :param X:
        :return:
        """
        z = np.dot(X,self.w_[1:])+self.w_[0]
        return z

