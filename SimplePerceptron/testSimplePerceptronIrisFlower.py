import pandas as pd
import  matplotlib.pyplot as plt
import  numpy as np
from SimplePerceptron import  SimplePerceptron
#Read the dataset


df = pd.read_csv("iris.data", header = None)

#the colums 0 and 2 are linearly separable, so that we can use to test the one layer perceptron
X = df.iloc[0:100, [0,2]].values

#We select Iris-Setosa and Iris-Versicolor.
Y = df.iloc[0:100, 4].values
Y = np.where(Y == 'Iris-setosa', -1,1)
# init the perceptron
ppn = SimplePerceptron(eta = 0.1, n_iter = 10)
#train with the vectors X and Y
ppn.fit_weights(X,Y)

predict = ppn.predict([7.1, 1.4])

#plot the error
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Update Number')

plt.tight_layout()
plt.show()

