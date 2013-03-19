import Image
import os
img=Image.open('D:\\cover2.png')


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
