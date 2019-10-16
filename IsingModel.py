from HopfieldErrorEstimation import HopfieldErrorEstimation
import numpy as np
import math
import random
from random import randint
from matplotlib import pyplot as plt
from pylab import cm
#GENERATE RANDOM MATRIX OF SIZE NXN
N = 20
hopfieldErrorEstimation = HopfieldErrorEstimation()
m = hopfieldErrorEstimation.generateRamdomPaterns(N,N)
#Initial Temperature
T = 5
range_temp = np.arange(0.01,T,0.01)
m = np.pad(m,[1,1])
Ef = 0
vectM = []

fig, ax = plt.subplots(1, 1)
im = ax.imshow(m, cmap=cm.binary, interpolation='nearest')
plt.axis('off')

for t in reversed(range_temp):
    Ei = Ef
    Ef = 0
    # plt.pause(0.0000000001)
    for i in range(2,N+1):
        im.set_data(m)
        fig.canvas.draw_idle()
        plt.pause(0.000000000000001)
        for j in range(2,N+1):
          Ef = Ef + (-0.5*m[i,j])*(m[i-1,j]+m[i+1,j]+m[i,j-1]+m[i,j+1])
    deltaE = Ef - Ei
    prob = math.exp(-deltaE/t)
    x = randint(1, N)
    y = randint(1, N)
    if deltaE < 0:
        m[x, y] = -1 * m[x, y]
    if deltaE > 0:
        if random.uniform(0, 1) < prob:
            m[x, y] = -1 * m[x, y]
    vectM.append(np.sum(m))

plt.plot(range_temp, vectM)
plt.show()









"""
N=10
m = rand(N,N)

for i=1:N
    for j:1:N
    m(i,j) = signo(m(i,j))
end
    end
for T:5:1:1  fijar los pasos pequeños todo lo adentro se itera mientras esto varía
    Ei = Ef

    Ef = 0;
    m = padarray(m, [1 1]);

for i = 2:N+1
    for j = 2: N+1
        Ef = Ef + (-0.5*m(i,j)*)
end
    end
        deltaE = Ef -Ei
        p = exponencua -(deltaE)

        #aca hacer la parte de sacar la exponecial
        if deltaE < 0
            acepto el cambio( cambio la matriz un valor que tomo aleatoriamente fuera de los valores)

        if deltaE > 0
            acepto el cambio con probalidad P
        #aca evaluar si el delta es mayor o menor
        #si es mnwbie a
        if delta

"""
