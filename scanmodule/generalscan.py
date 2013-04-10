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

def edgeboxscan(wlist,hlist):
    compressw = set(wlist)
    compressw.remove(0)
    compressh = set(hlist)
    compressh.remove(0)
    minedge = (min(compressh),min(compressw))
    maxedge = (max(compressh)+1,max(compressw)+1)
    return (minedge,maxedge)