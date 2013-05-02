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
#tmpimg=Image.open('D:\\tmp\\1.pdftmp\\1_bak.tif')
# tmpimg = tmpimg.convert(mode='L')
# tmpimgarray = np.array(tmpimg)-255
# imglayer = ndimage.binary_dilation(tmpimgarray, structure=np.ones((25,15))).astype(tmpimgarray.dtype)
# rawlayer = Image.fromarray(imglayer*255)
# rawlayer = ImageChops.invert(rawlayer)
# plt.imshow(rawlayer, cmap=plt.cm.gray)
# plt.show()
# rawlayer = pageprocess.pagerawanalysis(tmpimg,5,5,5,5)
tmpimg = tmpimg.convert(mode='1')
tmpimg = tmpimg.convert(mode='L')
rawlayer = np.array(tmpimg)-255
print 'array over'
# Image.fromarray(rawlayer*255,'L').save(filepath+'raw.tiff')
h,w = rawlayer.shape
verticalscan = generalscan.yprojection(rawlayer,0,h)
print 'yprojection over'
par = generalscan.rawscannew(verticalscan)

print 'yprojection rawscannew over'

# print 'calc full linebox'
# 
# linebox = []
# last=0
# for i in range(0,len(par)):
#     if i == 0:
#         a,b=par[i]
#         linebox.append([0,a-1])
#         linebox.append(par[i])
#         last=b
#     else:
#         a,b=par[i]
#         linebox.append([last,a-1])
#         linebox.append(par[i])
#         last=b

print 'xprojection start'

wordsbox = []
for j in par:
    j1,j2=j
    horizontalscan = generalscan.xprojection(rawlayer,j1,j2)
    a = generalscan.rawscannew(horizontalscan)        
    wordsret = []
    for i in a:
        i1,i2=i
        wordsret.append((i1,j1,i2,j2))
    wordsbox.append(wordsret)

print 'xprojection over, get words box'
#     if len(a)<1:
#         wordsret.append((0,j1,w,j2))
#         wordsbox.append(wordsret)
#         continue
print 'calc empty rectangles'

print 'calc full linebox'

linebox = []
last=0
for i in range(0,len(par)):
    if i == 0:
        a,b=par[i]
        linebox.append([0,a-1])
        last=b
    else:
        a,b=par[i]
        linebox.append([last,a-1])
        last=b

# blank=[]
# last=[]
# for i in par:
#     a,b=i
#     if len(last)<1:
#         blank.append([0,a])
#         last=i
#     else:
#         blank.append([last[1],a])
#         last=i
# print '2 over'
# vblank=[]
# for i in blank:
#     vblank.append(i[1]-i[0])
# 
# avglineb = (sum(vblank)/len(vblank)*0.6)
# if(avglineb>100):
#     avglineb=30
# ana = pageprocess.pagerawanalysis(tmpimg,avglineb,avglineb,5,5)
# Image.fromarray(ana*255,'L').save(filepath+'raw.tiff')
# 
# anayp = generalscan.yprojection(ana,0,ana.shape[0])
# anapar = generalscan.rawscannew(anayp)
#         
# 

# 
# for i in anapar:
#     for j in par:
#         a,b = i

# tfall = []
# for i in lineword:
#     tfline=[]
#     for j in i:
#         a,b,c,d = j
#         if ((c-a)*1.0/w)<0.1:
#             tfline.append('W')
#         elif ((c-a)*1.0/w)<0.3 and ((c-a)*1.0/w)>=0.1:
#             tfline.append('S')
#         elif ((c-a)*1.0/w) >=0.3:
#             tfline.append('C')
# #         tfline.append(((c-a)*1.0/w)>=0.2)
#     tfall.append(tfline)
# 
# valitf = []
# 
# for i in range(0,len(tfall)):
#     vali=[]
#     for j in range(0,len(tfall[i])):
#         a,b,c,d=lineword[i][j]
#         print str(a)+':'+str(b)+':'+str(c)+':'+str(d)
#         if tfall[i][j]=='C':
#             imga=tmpimg.transform ((c-a,d-b),Image.EXTENT ,(a,b,c,d))
#             imga = imga.convert(mode='1')
#             imga = imga.convert(mode='L')
#             imgarray = np.array(imga)-255
#             imgverticalscan = generalscan.yprojection(imgarray,0,imgarray.shape[0])
#             imgpar = generalscan.rawscannew(imgverticalscan)
#             if len(imgpar)<=1:
#                 vali.append('P')
#             else:
#                 vali.append('C')
#         else:
#             vali.append('K')
#     valitf.append(vali)
# totalblank=[]
# for j in lineword:
#     blanksqrt=[]
#     last=[]
#     avg=[]
#     for i in j:
#         a,b,c,d=i
#         avg.append(c-a)
#         if len(last)<1:
#             blanksqrt.append((0,b,a,d))
#             last=i
#         elif i== lineword[0][-1]:
#             blanksqrt.append((last[2],b,a,w))
#         else:
#             blanksqrt.append((last[2],b,a,d))
#             last=i
#     avg.remove(max(avg))
#     avg.remove(min(avg))
#     totalblank.append([i for i in blanksqrt if i[2]-i[0]>(sum(avg)/len(avg)*1.0)])


    
# for i in range(0,len(verticalscan)-1):
#     if (flag ==0 and verticalscan[i]==0):
#         flag=0
#     elif (flag ==0 and verticalscan[i]==1):
#         begin=i
#         flag=1
#     elif (flag==1 and verticalscan[i]==0):
#         par.append([begin,i-1])
#         flag=0
# 
# for j in par:
#     j1,j2=j
#     horizontalscan = generalscan.xprojection(rawlayer,j1,j2)
#     a = generalscan.rawscannew(horizontalscan)
#     for i in a:
#         i1,i2=i
#         img1=tmpimg.transform ((i2-i1,j2-j1),Image.EXTENT ,(i1,j1,i2,j2))
#         img1.save(filepath+str(j1)+'-'+str(i1)+'-'+str(j2)+'-'+str(i2)+'.tiff')
# 

    

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
