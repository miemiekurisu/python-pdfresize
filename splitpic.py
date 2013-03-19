# -*- coding: utf-8 -*-
listbw =scanpic(img,'w')
listtmp=[]
flag=0
for i in range(0,len(listbw)):
    a = listbw[i]
    if (flag==0) & (a!=0):
        listtmp.append(i)
        flag=1
    elif(flag!=0)&(a==0):
        listtmp.append(i)
        flag=0
        
print listtmp


for i in range(0,len(listtmp)):
    if i==0:
        row=img.transform((w,listtmp[i]+1),Image.EXTENT,(0,0,w,listtmp[i]+1))
    else:
        row=img.transform((w,listtmp[i]-listtmp[i-1]+1),Image.EXTENT,(0,listtmp[i-1]+1,w,listtmp[i]+2))
    path = 'D:\\tmp\\row'+str(i)+'.png'
    row.save(path)

rowhight=[]
whitehight=[]
for i in range(1,len(listtmp)):
	if i%2==1:
		rowhight.append((listtmp[i-1]+1,listtmp[i],listtmp[i]-listtmp[i-1]))
	else:
		whitehight.append((listtmp[i-1]+1,listtmp[i],listtmp[i]-listtmp[i-1]))

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
