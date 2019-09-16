from HopfieldErrorEstimation import HopfieldErrorEstimation
from Hopfield82 import Hopfield82
import numpy as np
hopfield = Hopfield82()
Number_of_Bits = 100
Number_of_Paterns = 102
hopfieldErrorEstimation = HopfieldErrorEstimation()
paternMatrix = hopfieldErrorEstimation.generateRamdomPaterns(Number_of_Bits,Number_of_Paterns)
weigth = hopfieldErrorEstimation.weigthMatrix(paternMatrix)
updated = hopfieldErrorEstimation.updateSync(weigth,paternMatrix)
error = hopfieldErrorEstimation.error(paternMatrix,updated)
print('ERROR:' + '\n')
print(error)

new_weigth = hopfieldErrorEstimation.deleteConexions(weigth)
v = (weigth == new_weigth)
print(list(v.flatten()).count(False))
print("Estimating the new Error")
new_updated = hopfieldErrorEstimation.updateSync(new_weigth,paternMatrix)
new_error = hopfieldErrorEstimation.error(paternMatrix,new_updated)
print('ERROR:' + '\n')
print(new_error)