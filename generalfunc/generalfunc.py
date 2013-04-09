import os

def statistic(anylist):
    anyset=set(anylist)
    rtlst={}
    for item in anyset:
        a=anylist.count(item)
        rtlst[item]=a
    return rtlst
    
def statisticavg(anylist, fix):
    anyset=set(anylist)
    maxnum=0
    heightofrow=0
    for item in anyset:
        a=anylist.count(item)
        if a>maxnum:
            maxnum=a
            heightofrow=item
    avgrange = (heightofrow*(1-fix), heightofrow*(1+fix))
    return avgrange

def getavg(dictline):
    dicavg = {}
    down,up =statisticavg(dictline.values(),0.2 )
    for i in dictline.keys():
        if (dictline[i]>=down) & (dictline[i]<=up):
            dicavg[i]=dictline[i]
    return dicavg


def listformaledge(image,rowscanlist,w,h):
    formalimglist=[]
    for i in rowscanlist.keys():
        imgtmp=image.transform ((w,rowscanlist.get(i)),Image.EXTENT ,(0,i,w,i+rowscanlist.get(i)))
        formalimglist.append(imgtmp)
    return formalimglist


def getfl(listscan,mod):
    fl=0
    a,b,c=0,0,0
    if mod=='f':
        a,b,c = 0, len(listscan)-1,1
    elif mod=='l':
        a,b,c = len(listscan)-1, 0, -1

    for i in range(a, b, c):
        if listscan[i]!=0:
            fl=listscan[i]
            break
        else:
            continue
    return fl

def calcF(anydic):
    sumblank=0
    sumblankno=0

    for item in anydic.keys():
        sumblank+=item*anydic.get(item)
        sumblankno+=anydic.get(item)
    return sumblank/sumblankno