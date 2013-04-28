import Image
import os
import ImageChops
import math

def rawscan(image , sf):
    coverbw=image.convert('1')
    w,h = coverbw.size
    pixline = []
    if sf =='w':
        for i in range(1,h,1):
            img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i,w,i+1))
            if 0 in list(img1.getdata()):
                pixline.append(i)
            else:
                pixline.append(0)
                continue
    elif  sf=='h':
        for i in range(1,w,1):
            img1=coverbw.transform ((1,h),Image.EXTENT ,(i,0,i+1,h))
            if 0 in list(img1.getdata()):
                pixline.append(i)
            else:
                pixline.append(0)
                continue
    return pixline

def scalbox(imglist):
    listtmp=[]
    flag=0
    for i in range(0,len(imglist)):
        a = imglist[i]
        if (flag==0) & (a!=0):
            listtmp.append(i)
            flag=1
        elif(flag!=0)&(a==0):
            listtmp.append(i)
            flag=0
    dictheight={}
    dictwhiteheight={}
    for i in range(1,len(listtmp)):
        if i%2==1:
            dictheight[listtmp[i-1]]=listtmp[i]-listtmp[i-1]
        else:
            dictwhiteheight[listtmp[i-1]]=listtmp[i]-listtmp[i-1]
    #listavg = getavg(dictheight)
    return dictheight,dictwhiteheight

def rawscannew(verticalscan):
    begin=0
    flag=0
    par = []
    
    for i in range(0,len(verticalscan)):
        if (flag ==0 and verticalscan[i]==0):
            flag=0
#             print 'A begin='+str(begin)
#             print 'A flag='+str(flag)
        elif (flag ==0 and verticalscan[i]==1):
            begin=i
            flag=1
#             print 'B begin='+str(begin)
#             print 'B flag='+str(flag)
        elif (flag==1 and verticalscan[i]==0):
            par.append([begin,i+1])
            flag=0
#             print 'C begin='+str(begin)
#             print 'C flag='+str(flag)
    return par

def yprojection(scanarray):
    verticalscan=[]
    for i in range(0,len(scanarray)):
        if 1 in scanarray[i]:
            verticalscan.append(1)
        else:
            verticalscan.append(0)
    return verticalscan
            
def xprojection(scanarray,par1,par2):    
    horizontalscan=[]
    for i in range(0,len(scanarray[par1])):
        if 1 in scanarray[par1:par2,i]:
            horizontalscan.append(1)
        else:
            horizontalscan.append(0)
    return horizontalscan
    
def edgeboxscan(wlist,hlist):
    compressw = set(wlist)
    compressw.remove(0)
    compressh = set(hlist)
    compressh.remove(0)
    minedge = (min(compressh),min(compressw))
    maxedge = (max(compressh)+1,max(compressw)+1)
    return (minedge,maxedge)