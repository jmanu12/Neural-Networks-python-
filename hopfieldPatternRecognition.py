import matplotlib as matplotlib
import numpy as np
from tqdm import tqdm
from Hopfield82 import Hopfield82
from processData import ProcessData

# ############### READ DATA ######################
# picture = ProcessData.read_image('Images/paloma.bmp')
#we read the picture as a vector of the individual file
#print(picture)

new_data = ProcessData()
data_trainig = new_data.read_train_path('Images/','*.bmp')
input_vector = new_data.read_image('Images/paloma.bmp')

# ############### LEARNING ######################
hopfield = Hopfield82()
weigth_matrix = hopfield.create_weight_matrix(data_trainig)
print(weigth_matrix)
# ############### TEST ######################










    #https://github.com/yosukekatada/Hopfield_network/blob/master/hopfield.py
