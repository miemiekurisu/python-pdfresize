import Image
import os
import math
from generalfunc import glfunc
import scanmodule
from preprocess import precropblank
from scanmodule import generalscan
import glob
import ImageChops
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

def pagerawanalysis(tmpimg,boxx,boxy,closex,closey):
    
    tmpimg = tmpimg.convert(mode='L')
    tmpimgarray = np.array(tmpimg)-255
    imglayer = ndimage.binary_dilation(tmpimgarray, structure=np.ones((boxx,boxy))).astype(tmpimgarray.dtype)
    imglayer = ndimage.binary_closing(tmpimgarray, structure=np.ones((closex,closey))).astype(tmpimgarray.dtype)

    return imglayer