
import os
import glob
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
#import cv2

from Funcs.tools import sixteen_bits2eight_bits
Datadir_raw = './Data/Raw/'
Datadir_8bit = './Data/8bit/'
Hist_dir = './Data/Histograms/'


for image in os.listdir(Datadir_raw):

    print(Datadir_raw+image)
    input_image = Image.open(Datadir_raw + image)
    image_16 = np.array(input_image)
    im_8bit = sixteen_bits2eight_bits(Datadir_raw+image)
    plt.imsave(Datadir_8bit+image, im_8bit)
    # plt.show()
    # Mx = np.max(image_16.flatten())
    # Mn = np.min(image_16.flatten())
    # plt.hist(image_16.ravel(), 100, [Mn , Mx])
    # plt.title('Histogram for 16bit picture')
    # plt.savefig(Hist_dir + image)
    # Q1 = np.quantile(image_16.flatten(), 0.25)
    # Q3=np.quantile(image_16.flatten(), 0.75)
    # Outliner_Threshold = Q3+1.5*(Q3-Q1)
