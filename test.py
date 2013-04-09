import Image
import os
import generalfunc
import scanmodule
from preprocess import precropblank
from scanmodule import generalscan
import math

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
testimg = precropblank.overlying(filepath,filename,10,600,None,pathflag)
tmp=generalscan.rawscan(testimg,'w')
tm1,tm2 = generalscan.scalbox(tmp)
l=tm1.keys()
l.sort()

        
p52=Image.open(picname+'52.png')
p52s=generalscan.rawscan(p52,'w')
p52test=[]
for i in l:
    listl=p52s[i-1:i+tm1.get(i)-1]
    p52test.append(listl)
    
p52box=[]
for i in p52test:
    p52a,p52b=generalscan.scalbox(i)
    p52box.append(p52a)


    