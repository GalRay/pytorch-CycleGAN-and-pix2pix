import numpy as np
from PIL import Image

def sixteen_bits2eight_bits(path):
    # Pseudo colouring the 16 bit images
    input_img = Image.open(path)
    pixel = np.array(input_img)
    ####
    Q1 = np.quantile(pixel.flatten(), 0.25)
    Q3 = np.quantile(pixel.flatten(), 0.75)
    Outliner_Threshold = Q3+3*(Q3-Q1)
    pixel[pixel>Outliner_Threshold] = Outliner_Threshold
    pixel = (pixel - np.min(pixel)) / (Outliner_Threshold-np.min(pixel))
    pixel = np.rint(pixel * 255)
    pixel2 = np.zeros((np.array(pixel).shape[0], np.array(pixel).shape[1], 3))
    pixel2[:, :, 0] = pixel
    pixel2[:, :, 1] = pixel
    pixel2[:, :, 2] = pixel
    pixel_colored = np.uint8(pixel2)
    return pixel_colored

