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

#input_vector = new_data.read_image('Images/paloma.bmp')

# ############### LEARNING ######################
hopfield = Hopfield82()
# read the trainig data located in the folder perro
data_trainig = new_data.read_train_path('Images/','*.bmp')
# calculate the weigth matrix
weigth_matrix = hopfield.create_weight_matrix(data_trainig)
test = new_data.read_image('Images/perro2.bmp')
#The test set
predicted = hopfield.update(test, weigth_matrix, 30, 0, False)

print(predicted)
    #model.plot_weights()

#Generate a vector to update

# ############### TEST ######################
"""
#create  a new folder with data 
input_vector = new_data.read_image('Images/perro.bmp')
new_data.generate_ramdom_data(input_vector, 0.3, 8,'perro' )
"""










    #https://github.com/yosukekatada/Hopfield_network/blob/master/hopfield.py
