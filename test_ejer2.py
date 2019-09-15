from error import ejercicio2
import numpy as np
ejer2 = ejercicio2()
paternMatrix = ejer2.generatePaterns(100,100)
weigth = ejer2.weigthMatrix(paternMatrix)
updated = ejer2.updateAsyn(weigth,paternMatrix)
error = ejer2.error(paternMatrix,updated)
print(error)

