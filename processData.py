import cv2
import numpy as np
import os, glob
import shutil
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.cm as cm


class ProcessData:

    def read_image(self, dataImput_path):
        """
          read a path file and return a vector of 1 and -1 values(First we read as a Matrix the)
        """
        # read image as grayscale. Set second parameter to 1 if rgb is required
        datainput = np.squeeze(np.asarray(cv2.imread(dataImput_path, 0)))
        # change the white from 255 to -1 and
        datainput = np.where(datainput == 255, -1, datainput)
        # black from 0 to 1  and changes from matrix to vector
        datainput = np.array(np.where(datainput == 0, 1, datainput)).flatten()

        return datainput

    def read_train_path(self, path, extension):
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
                        if datainput.size > 1 and (file == 'panda.bmp' or file == 'v.bmp' or file == 'perro.bmp'):
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

    def generate_ramdom_data(self, data_input, corruption_level, num_random_item, path, name_file):

        if num_random_item > 0 and data_input is not None:
            if corruption_level is None:
                corruption_level = 0.3
            directorio =  str(path)
            try:
                if not os.path.exists('./'+path):
                    original_umask = os.umask(0)
                    os.makedirs(directorio, 0o777)
            except:
                print("La creación del directorio %s falló" % directorio)
            else:
                print("Se ha creado el directorio: %s " % directorio)
            num = 0
            for k in range(num_random_item):
                num = num + 1
                generate_random = np.copy(data_input)
                inv = np.random.binomial(n=1, p=corruption_level, size=len(data_input))
                for i, v in enumerate(data_input):
                    if inv[i]:
                        generate_random[i] = -1 * v
                plt.imsave(name_file+str(num)+".bmp", np.array(generate_random).reshape(50, 50), cmap=cm.gray)
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
    def create_test_folder(self,folder_output_name, folder_imput_data):
        for file in self.list_files(folder_imput_data,".bmp"):
            if file != None:
                imput_vector = self.read_image(folder_imput_data+file)
                self.generate_ramdom_data(imput_vector,0.3,1,folder_output_name,file[:-4])





