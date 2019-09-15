import cv2
import numpy as np
import os, glob
import matplotlib.pyplot as plt
from time import sleep
import sys
from pylab import imshow, cm, figure, axis


class ImageIO:

    def read_image_as_vector(self, dataImput_path):
        """
        :param dataImput_path: path to read the image
        :return datainput : a row vector with populated with -1 to 255 and 1 to 0
        """
        # read image as grayscale. Set second parameter to 1 if rgb is required
        datainput = np.squeeze(np.asarray(cv2.imread(dataImput_path, 0)))
        # change the white from 255 to -1 and
        datainput = np.where(datainput == 255, -1, datainput)
        # black from 0 to 1  and changes from matrix to vector
        datainput = np.array(np.where(datainput == 0, 1, datainput)).flatten()

        return datainput

    def read_train_data(self, path, extension):
        """
        :param path: to reead the image
        :param extension file
        :return: a matrix with the images train data in each row
        """
        print("READ TRAIN DATA" + '\n')
        self.progress()
        if not os.path.exists(path):
            print("The path does't exist!")
        else:
            os.chdir(path)
            data_matrix = []
            for file in glob.glob(extension):
                if file is not None:
                    try:
                        datainput = np.squeeze(np.asarray(cv2.imread(file, 0)))
                        # change the white from 255 to -1 and
                        datainput = np.where(datainput == 255, -1, datainput)
                        # black from 0 to 1
                        datainput = np.where(datainput == 0, 1, datainput)

                        if datainput.size > 1:
                            # change the matrix to vector
                            row_data = np.array(datainput).flatten()
                            data_matrix.append(row_data)
                        # img.show()
                        # del img
                    except IOError:
                        pass
            data_matrix = np.array(data_matrix)
            data_matrix = np.asmatrix(data_matrix)
        return data_matrix

    def generate_ramdom_test_image(self, data_input, corruption_level, num_random_item, name_file):
        """
        :param data_input: row vector that represent an image
        :param corruption_level:  the corruption level to generate a new image
        :param num_random_item: the number of the outputs that we want
        :param name_file: the name file
        :return: save the test image in the following path: 'Images/testData/'
        """
        print("GENERATING AND SAVING CORRUPTED IMAGES FOR " + '\n'+name_file)
        self.progress()
        if num_random_item > 0 and data_input is not None:
            if corruption_level is None:
                corruption_level = 0.8

            num = 0
            for k in range(num_random_item):
                num = num + 1
                generate_random = np.copy(data_input)
                inv = np.random.binomial(n=1, p=corruption_level, size=len(data_input))
                for i, v in enumerate(data_input):
                    if inv[i]:
                        generate_random[i] = -1 * v
                plt.imsave('Images/testData/'+name_file+str(num)+".bmp", np.array(generate_random).reshape(50, 50), cmap=cm.gray)
            return 1

        else:
            print("error, is not posible create data")
            return 0

    def list_files(self,path, extension):
        """
        :param path: directory to show the files
        :param extension: file extension
        :return: a vector with the name of the files
        """
        files = os.listdir(path) #[f for f in glob.glob(path + "**/*"+extension, recursive=False)]
        return files
    def create_test_data(self, folder_imput_data):
        """
        :param folder_imput_data: directory with the input data
        :return:generate the test data with the image located in folder_imput_data
        """
        for file in self.list_files(folder_imput_data,".bmp"):
            if file != None:
                imput_vector = self.read_image_as_vector(folder_imput_data+file)
                self.generate_ramdom_test_image(imput_vector,0.8,1,file[:-4])

    def display(self,imgLr,imgRr):
        fig = figure()
        a = fig.add_subplot(1, 2, 1)
        imgplot = imshow(imgLr.reshape((50, 50)), cmap=cm.binary, interpolation='nearest')
        a.set_title('Input')
        axis('off')
        a = fig.add_subplot(1, 2, 2)
        imgplot = imshow(imgRr.reshape((50, 50)), cmap=cm.binary, interpolation='nearest')
        imgplot.set_clim(0.0, 0.7)
        a.set_title('Predicted')
        axis('off')
        plt.show()

    def resize(self, path, name):
        from PIL import Image
        basewidth = 50
        img = Image.open(path)
        hsize = 50
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img.save(name)

    def progress(self):
        for i in range(21):
            sys.stdout.write('\r')
            # the exact output you're looking for:
            sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
            sys.stdout.flush()
            sleep(0.25)