import cv2
import numpy as np
import os, glob
from PIL import Image
from pathlib import Path


class ProcessData:

    def read_image(self, dataImput_path):
        """
          read a path file and return a vector of 1 and -1 values(First we read as a Matrix the)
        """
        # read image as grayscale. Set second parameter to 1 if rgb is required
        datainput = np.squeeze(np.asarray(cv2.imread(dataImput_path, 0)))
        # change the white from 255 to -1 and
        datainput = np.where(datainput == 255, -1, datainput)
        # black from 0 to 1
        datainput = np.where(datainput == 0, 1, datainput)
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
                        if datainput.size > 1 and (file == 'panda.bmp' or file == 'v.bmp'  or file == 'perro.bmp'):
                            data_matrix.append(datainput)
                        # img.show()
                        # del img
                    except IOError:
                        pass
            data_matrix = np.array(data_matrix)
            print(data_matrix.shape)
        return data_matrix
