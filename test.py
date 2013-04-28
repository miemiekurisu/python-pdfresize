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


for i in picfiles:
    os.remove(i)
pages = precropblank.extracttoimg()


tmpimg=Image.open(picname+'1'+'.tiff')
#tmpimg=Image.open('D:\\tmp\\1.pdftmp\\1_bak.tif')
# tmpimg = tmpimg.convert(mode='L')
# tmpimgarray = np.array(tmpimg)-255
# imglayer = ndimage.binary_dilation(tmpimgarray, structure=np.ones((25,15))).astype(tmpimgarray.dtype)
# rawlayer = Image.fromarray(imglayer*255)
# rawlayer = ImageChops.invert(rawlayer)
# plt.imshow(rawlayer, cmap=plt.cm.gray)
# plt.show()
rawlayer = pageprocess.pagerawanalysis(tmpimg,5,5,6,6)

verticalscan = generalscan.yprojection(rawlayer)

par = generalscan.rawscannew(verticalscan)
# for i in range(0,len(verticalscan)-1):
#     if (flag ==0 and verticalscan[i]==0):
#         flag=0
#     elif (flag ==0 and verticalscan[i]==1):
#         begin=i
#         flag=1
#     elif (flag==1 and verticalscan[i]==0):
#         par.append([begin,i-1])
#         flag=0

for j in par:
    j1,j2=j
    horizontalscan = generalscan.xprojection(rawlayer,j1,j2)
    a = generalscan.rawscannew(horizontalscan)
    for i in a:
        i1,i2=i
        img1=tmpimg.transform ((i2-i1,j2-j1),Image.EXTENT ,(i1,j1,i2,j2))
        img1.save('D:\\tmp\\'+str(j1)+'-'+str(i1)+'-'+str(j2)+'-'+str(i2)+'.tiff')

if len(a)<=4:
    #todo
    #recursion if <=4, for multiple columns
    None
    

# # 
# # tmpimgw = generalscan.rawscan(rawlayer,'w')
# # x,y = rawlayer.size
# # 
# # boximgw,lost = generalscan.scalbox(tmpimgw)
# # layerlist = {}
# # tmpkey = boximgw.keys()
# # tmpkey.sort()
# # for i in tmpkey:
# #     img1=rawlayer.transform ((x,boximgw.get(i)),Image.EXTENT ,(0,i,x,i+boximgw.get(i)))
# #     layerlist[i]=img1
# # 
# # res = {}
# # tmpkey = layerlist.keys()
# # tmpkey.sort()
# # for i in tmpkey:
# #     tmpbox,lost = generalscan.scalbox(generalscan.rawscan(layerlist.get(i),'h'))
# #     res[i]=tmpbox
# #     
# # boxs = []
# # tmpkey = boximgw.keys()
# # tmpkey.sort()
# # for i in tmpkey:
# #     hight = boximgw.get(i)
# #     for j in res.get(i).keys():
# #         blockbox = [j,i,j+res.get(i).get(j),i+boximgw.get(i)]
# #         boxs.append(blockbox)
# #         
# # imga={}
# # for i in boxs:
# #     a,b,c,d = i
# #     img1=tmpimg.transform ((c-a,d-b),Image.EXTENT,(a,b,c,d))
# #     imga[((a,b),(c,d))]=img1


        
# for i in range(0,len(imga.values())-1):
#     imga.values()[i].save('D:\\'+str(i)+'.png')

# tmplst = list(tmpimg.getdata())
# tmpimg1=ImageChops.invert(tmpimg)
# tmplst1=list(tmpimg1.getdata())
# a,b = tmpimg1.size
# for i in (0,a*b,b-1):
#     sum(tmplst1[
# all = []
# for i in range(1,260):
#     tmpimg=Image.open(picname+str(i)+'.png')
#     a=generalscan.rawscan(tmpimg,'w')
#     all.append(a.count(0))
#    print i

# Ex=sum(all)/float(260)
# v=sum((float(i)-float(Ex))**2 for i in all)/(len(all)-1)
# form = [i+1 for i in range(1,259) if abs(all[i]-Ex)<math.sqrt(v)]
# 
# picspath = filepath+filename+'tmp'+pathflag
# 
# imageall=precropblank.overlying(picspath,filename,form,'1')
# 
# imageall.save(picspath+filename+'-'+'test.png')



# Ex=sum( [i for i in range(1,2479)])/float(2479)
# variance=[]
# for i in range(1,670):
#     tmpimg=Image.open(picname+str(i)+'.png')
#     histmp = glfunc.histogramcalc(tmpimg,'y')
#     v=sum((float(i)-float(Ex))**2 for i in histmp)
#     variance.append(v)
# avg = sum(i for i in variance)/len(variance)
# st = [i+1 for i in range(0,len(variance)-1) if abs(variance[i]-avg)/avg<0.01]]



# testimg = precropblank.overlying(filepath,filename,10,600,None,pathflag)
# tmp=generalscan.rawscan(testimg,'w')
# tm1,tm2 = generalscan.scalbox(tmp)
# l=tm1.keys()
# l.sort()
# 
#         
# p53=Image.open(picname+'53.png')
# p53s=generalscan.rawscan(p53,'w')
# p53test=[]
# for i in l:
#     listl=p53s[i-1:i+tm1.get(i)-1]
#     p53test.append(listl)
#     
# p53box=[]
# for i in p53test:
#     p53a,p53b=generalscan.scalbox(i)
#     p53box.append(p53a)
# for i in range (1,int(pages)+1):
#     tmppic=Image.open(picname+str(i)+'.png')
#     tmppic=precropblank.cropblank(tmppic)
#     tmppic.save(picname+str(i)+'.png')
