import matplotlib.pyplot as plt
from skimage.filter import canny
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

if(os.sys.platform=='win32'):
    gspath = 'gswin32c.exe'
    filepath= 'D:\\tmp\\'
    pathflag='\\'
    filename = '1.pdf'
else:
    gspath = '/usr/local/bin/gs'
    filepath = '/Users/chris/Dev/tmp/'
    pathflag='/'
    filename = '1.pdf'


picname = filepath+filename+'tmp'+pathflag+filename+'-'
picfiles = glob.glob(filepath+filename+'tmp'+pathflag+filename+'-*')

tmpimg=Image.open(picname+'95'+'.tiff')
tmpimgar = np.array(tmpimg)
edges = canny(tmpimgar, 3, 0.5, 1)
edges1=edges.astype(np.int)
edgesimg = Image.fromarray((edges1*-1+1)*255,mode='L')
edgesimg.save('d:\\tmp\\edge1.tiff')
# plt.imshow(edges,cmap=plt.cm.gray)
# plt.axis('off')
# plt.show()

