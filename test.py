import Image
import os
import math
from generalfunc import glfunc
import scanmodule
from preprocess import precropblank
from scanmodule import generalscan
import glob


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
#picfiles = glob.glob(filepath+filename+'tmp'+pathflag+filename+'-*')
# for i in picfiles:
#     os.remove(i)
# pages = precropblank.extracttoimg()

Ex=sum( [i for i in range(1,2479)])/float(2479)
variance=[]
for i in range(1,670):
    tmpimg=Image.open(picname+str(i)+'.png')
    histmp = glfunc.histogramcalc(tmpimg,'y')
    v=sum((float(i)-float(Ex))**2 for i in histmp)
    variance.append(v)
avg = sum(i for i in variance)/len(variance)
st = [i+1 for i in range(0,len(variance)-1) if abs(variance[i]-avg)/avg<0.01]
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
