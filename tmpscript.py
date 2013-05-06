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
from scanmodule import pageprocess


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


# for i in picfiles:
#     os.remove(i)
# pages = precropblank.extracttoimg()


tmpimg=Image.open(picname+'95'+'.tiff')
print 'readover'

w,h = tmpimg.size

for i in range(1,20):
    for j in range(1,20):
        w1= int(round(w*(i*0.05-0.05)))
        h1= int(round(h*(j*0.05-0.05)))
        w2= int(round(w*i*0.05))
        h2= int(round(h*i*0.05))
        tmpimg.transform((int(round(w*0.05)),int(round(h*0.05))),Image.EXTENT ,(w1,h1,w2,h2)).save(filepath+str(i)+'-'+str(j)+'crop.tiff')

tmpimg = tmpimg.convert(mode='1')
tmpimg = tmpimg.convert(mode='L')
rawlayer = np.array(tmpimg)-255
print 'array over'
Image.fromarray(rawlayer*255,'L').save(filepath+'raw.tiff')
h,w = rawlayer.shape

ypro = generalscan.yprojection(rawlayer,0,h)
yprolist = generalscan.rawscannew(ypro)
print 'yprojection over'

xpro = generalscan.xprojection(rawlayer,0,w)
xprolist = generalscan.rawscannew(xpro)

print 'xprojection over'

bound = [xprolist[0][0],yprolist[0][0],xprolist[-1][1],yprolist[-1][1]]

tmpimg.transform((bound[2]-bound[0],bound[3]-bound[1]),Image.EXTENT ,(bound)).save(filepath+'crop.tiff')
print 'find bound'

total=[]
for i in yprolist:
    a,b = i
    total.append(b-a)
total.remove(max(total))
total.remove(min(total))
avg=sum(total)/len(total)*1.0

page = pageprocess.pagerawanalysis(tmpimg,avg*0.66,avg*0.66,0,0)
Image.fromarray(page*255).transform((bound[2]-bound[0],bound[3]-bound[1]),Image.EXTENT ,(bound)).save(filepath+'page.tiff')

ypage = generalscan.yprojection(page,0,w)
ypagepro = generalscan.rawscannew(ypage)

obs = []
for j in ypagepro:
    j1,j2=j
    horizontalscan = generalscan.xprojection(page,j1,j2)
    a = generalscan.rawscannew(horizontalscan)        
    for i in a:
        i1,i2=i
        obs.append((i1,j1,i2,j2))

for i in obs:
    a,b,c,d=i
    Image.fromarray(page*255).transform((c-a,d-b),Image.EXTENT ,i).save(filepath+str(a+b+c+d)+'page.tiff')