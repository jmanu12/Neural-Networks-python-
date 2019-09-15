from Hopfield82 import Hopfield82
from ImageIO import ImageIO

new_data = ImageIO()



##############################GENERATE CORRUPTED IMAGES#################################

#list_files = new_data.create_test_data('Images/trainData/')


# ########################## HOPFIELD TEST##############################################
hopfield = Hopfield82()
plot = Hopfield82()
#IMAGE TO BE TESTED
test_image  = 'Images/testData/torero1.bmp'
new_data2 = ImageIO()
#read the value of the corrupted image
test_plot_image = new_data2.read_image_as_vector(test_image)
test = new_data.read_image_as_vector(test_image)
# read the trainig data located in the folder 'Images/trainData'
data_trainig = new_data.read_train_data('Images/trainData','*.bmp')
# calculate the weigth matrix
weigth_matrix = hopfield.create_weight_matrix(data_trainig)
#Predict
predicted,energy = hopfield.asynchronousTesting(weigth_matrix,test )
print('ENERGY')
print(energy)

new_data2.display(test_plot_image,predicted)
