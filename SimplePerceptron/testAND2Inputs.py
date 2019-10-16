import pandas as pd
import  matplotlib.pyplot as plt
import  numpy as np
from SimplePerceptron import  SimplePerceptron
#Train data
X = np.array([
    [1.0,1.0],
    [1.0,-1.0],
    [-1.0,1.0],
    [-1.0,-1.0]
    ])

#outputs
Y = np.array([1.0,-1.0,-1.0,-1.0])
# init the perceptron
ppn = SimplePerceptron(eta = 0.1, n_iter = 10)
#train with the vectors X and Y
ppn.fit_weights(X,Y)

predictNewInput = ppn.predict([-1.0, 1.0])
print(predictNewInput)

#plot the error
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel('Epochs')
plt.ylabel('Update Number')

plt.tight_layout()
plt.show()

