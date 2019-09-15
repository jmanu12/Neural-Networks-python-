#AVADNJAL
import numpy as np

class ejercicio2:

    def weigthMatrix(self,paternMatrix):
        W = 1/100*(np.dot(paternMatrix, (np.transpose(paternMatrix))) - 100*np.identity(100,dtype=float))
        return W
    def generatePaterns(self, N ,M ):
        random_array = np.random.randint(2, size=(N,M))
        random_array = np.where(random_array == 0, -1 ,random_array)
        return random_array
    def updateAsyn(self, weigth_matrix, patern_matrix):
            update = np.dot(weigth_matrix, patern_matrix)
            update = np.where(update < 0, -1, update)
            update = np.where(update>0,1,update)
            return update
    def error(self, update_paterns, paterns):
        #para encontrar el error comparo estas dos matrices y
        v = (update_paterns == paterns)
        return list(v.flatten()).count(False)/(100*100)










