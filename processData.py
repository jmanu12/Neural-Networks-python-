import cv2
import numpy as np
import os, glob
from PIL import Image


class ProcessData:

    def read_image(dataImput_path):
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

    def read_train_path(self, extension):
        if not os.path.exists(self):
            print("The path does't exist!")
        else:
            os.chdir(self)
            for file in glob.glob(extension):
                if file is not None:
                    print(file)
                    try:
                        # Relative Path
                        img = Image.open(file)
                        #img.show()
                        # del img
                    except IOError:
                        pass
        return
