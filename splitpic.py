# -*- coding: utf-8 -*-
import Image
import os
import ImageChops
img=Image.open('D:\\cover2.png')
#img = Image.open('/Users/chris/Dev/github/python-pdfresize/cover2.png')
w,h=img.size
def scanpic(image , sf):
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

listbw =scanpic(img,'w')


def rowscan(imglist):
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

def statistic(anylist):
    anyset=set(anylist)
    rtlst={}
    for item in anyset:
        a=anylist.count(item)
        rtlst[item]=a
    return rtlst

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

line,whiteline=rowscan(listbw)
avg = getavg(line)
avgrowh1,avgrowh2 = statisticavg(line.values(),0.2)
flist=[]
edlist=[]
imglist=[]
startisA={}
startisN={}
scanrowlist=[]
for i in line.keys():
    imagetemp=img.transform((w,line.get(i)),Image.EXTENT,(0,i,w,i+line.get(i)))
    imglist.append(imagetemp)
    scanh=scanpic(imagetemp,'h')
    scanrow,scann = rowscan(scanh)
    scanrowlist.append(scanrow)
    avgtmp=statistic(scanrow.values())
    avgtmpno=statistic(scann.values())
    for item in avgtmp.keys():
        if startisA.get(item) is None:
            startisA[item]=avgtmp.get(item)
        else:
            startisA[item]=startisA[item]+avgtmp.get(item)
    for item in avgtmpno.keys():
        if startisN.get(item) is None:
            startisN[item]=avgtmpno.get(item)
        else:
            startisN[item]=startisN[item]+avgtmpno.get(item)

a1,a2=statisticavg(flist,0.01)
e1,e2=statisticavg(edlist,0.01)


FAW = calcF(startisA)
FAD = calcF(startisN)


print FAW, FAD

temppics=[]
for item in scann.keys():
    if scann.get(item)<FAD:
        del scann[item]
        
aa=scann.keys()
aa.append(0)
aa.sort()

scann[0]=0


for i in range(1,len(aa)):
     imagetempaa=imagetemp.transform((aa[i]-aa[i-1],25),Image.EXTENT,(aa[i-1]+scann.get(aa[i-1]),0,aa[i]+1,25))
     temppics.append(imagetempaa)
     
#os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=20 -r150 -sOutputFile="D:\\tmp\\cover-%d.png" "D:\\1.pdf"')

imglist=[]
imageall = None
for i in range(1,670):
    if i==1:
        imageall=Image.open('D:\\tmp\\pic-'+str(i)+'.png')
        continue
    else:
        imgtmp=Image.open('D:\\tmp\\pic-'+str(i)+'.png')
        imageall=ImageChops.darker(imgtmp,imageall)
        imgtmp=None
        continue
#for i in range(0,len(temppics)):
#   temppics[i].save('D:\\tmp\\'+str(i)+'.png')

##for i in line.keys():
##    rowh = line.get(i)
##    imagetemp=img.transform((w,rowh),Image.EXTENT,(0,i,w,i+rowh))
##    scanh=scanpic(imagetemp,'h')
##    f = getfl(scanh,'f')
##    e = getfl(scanh,'l')
   ## if (scanh>=
##for i in range(0,len(listtmp)):
##    if i==0:
##        row=img.transform((w,listtmp[i]+1),Image.EXTENT,(0,0,w,listtmp[i]+1))
##    else:
##        row=img.transform((w,listtmp[i]-listtmp[i-1]+1),Image.EXTENT,(0,listtmp[i-1]+1,w,listtmp[i]+2))
##    path = 'D:\\tmp\\row'+str(i)+'.png'
##    row.save(path)



##use data structure (words/pic,indantation,(left top x, left top y, right bottom x, right bottom y))
## 取平均行高, 偏差在±20%, 设为文字行
## 合并相邻的图片行,并重新计算图片行大小
## 第i行文字的处理:
## 手动指定是否存在页眉页脚,栏数, 边栏
## 统计总行数n的起始A1=(s1,s2...sn),结束A2=(e1,e2...en)
## 选择最多的sk,设置为左边界标杆S, 边界起始偏差允许在±10%, 选择最多的边界结束E,偏差允许在±10%
##
## 图片维持原比例或缩小比例至适合标准行长
## i=0 时, 若指定存在页眉, 则si左边界重定为左边界标杆. 若s0超过最长长度且不可截断,
## 则调整s0大小,使适合最长长度.若不存在页眉, 则处理方式同i=[1,n-1]
## i=[1,n-1]时, 保持S与si位置,若si超过显示设置最长长度,则进行截断重排,
## 重排后行首位置取决于si与S的相对位置, 若
##
##2. if height deviation < ±40% , regards it like same simple characters line
## 以上内容完全想错了, 但是scanpic函数的一部分可以复用
## 在没有做logic layout analysis之前,无法得知哪些是页眉,页脚,侧边栏
## 首先做版面无关的扫描,自顶向下横向逐行扫描
## 需要取得的数据:
## 1. 物理每行高度
## 2. 物理行间距
## 将整个图片分割为物理行
## 每个物理行从左向右纵向逐行扫描
## 需要取得的数据:
## 1. 物理行起始距离页左边距
## 2. 物理行结束距离页右边距
## 3. 将物理行纵向分割开, 分割为"图框/间距/图框..."的形式
## 版面分析基于某些事实和假设:
## 1. 假设正文文字部分行开始和行结束都在一个给定的标准范围之内
## 2. 假设, 正文占页面绝大多数内容
## 3. 事实,字符间距小于可断行间距
## 我忽然想到是不是先可以统计一下每一行起始和每一行结束
## 去掉不规律的部分做重扫描, 如果基于假设2,去掉不规律部分就是正常的正文版面
## 然后就只需要处理不规律的部分了, 对不规律的部分做重扫描, 确定是何种类型的不规律
## 不规律的类型:标题,页眉, 页脚, 两侧边栏, 图片
## 这样定义不规律部分, 基于假设1, 如果(起始 or 结束) and 行高,行间距判定为false
## 现在到了判断纵向标准起始和标准结束的地方,与横向判断逻辑上一致
## 2013/03/20 觉得既然这样不如把一页化为image list,然后走循环去判断标准行高和标准行起始,标准行结束
## 2013/04/02 是不是要自底向上? 是不是要自底向上?!
## 我需要一个数据结构, 让我不要做多余的事情.
## 最后整件事情还是归结为"怎么能知道这块区域和其他区域不一样?"
## 要描绘出正文部分和其他部分, 只将正文部分重排就可以了,图片按比例缩小(如果需要)
## 标准起始,标准结束,第一行标准行,最末标准标准行, 若其中任意行超过标准行长, 且标准行长之后存在不连通性
## 则认为之后部分都为其他部分, 以此描绘标准正文区域.
## 这是一个递归的过程,但是该死的是我要写成迭代
## 我怎么知道是页眉,页脚和左右边栏, 这些东西有明显特征么?
