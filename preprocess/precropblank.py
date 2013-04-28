import Image
import os
import ImageChops
from scanmodule import generalscan

global gspath
global temppath
global filepath
global filename
global pathflag

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

def pdffileinput():
    filepath = raw_input('Please input file path:')
    flag='/'
    if (os.sys.platform=='win32'):
        split=filepath.split('\\')
        flag='\\'
    else:
        split=filepath.split('/')
        
    if split[-1].lower().find('pdf')!=-1 :
        filename=split[-1]
    split.remove(split[-1])
    filepath=flag.join(split)
    return filepath,filename

def basesetup():
    global gspath 
    gspath = raw_input('Please input ghostscript binnary path:')
    if(os.sys.platform=='win32'):
        gspath=gspath+'/gswin32c.exe'
    else:
        gspath=gspath+'/gs'
    
    flag=raw_input('Do you want to set up temp file path? (yes/no):')
    if flag.lower()=='yes':
        global temppath
        temppath =row_input('Please input temp file path:')
    elif flag.lower()=='no':
        None
    else:
        print 'Error'

def propertyfile(valuedict):
    None

def extracttoimg(): #static arg for developing/testing
    if(os.sys.platform=='win32'):
        gspath = 'gswin32c.exe'
        filepath= 'D:\\tmp\\'
        flag='\\'
    else:
        gspath = '/usr/local/bin/gs'
        filepath = '/Users/chris/Dev/tmp/'
        flag='/'
    filename = '1.pdf'
    pagestart=1
    pageend=670
    dpi=150
    
    cmdstr1=' -q -sDEVICE=pnggray -dBATCH -dNOPAUSE '
    firstpage = '-dFirstPage='+str(pagestart)+' '
    lastpage = '-dLastPage='+str(pageend)+' '
    r = '-r'+str(dpi)+' '
    outfile = '-sOutputFile="'+filepath+filename+'tmp'+flag+filename+'-%d.tiff" '
    
    if os.path.isdir(filepath+filename+'tmp'): 
        pass 
    else: 
        os.mkdir(filepath+filename+'tmp')
    os.system(gspath+cmdstr1+firstpage+lastpage+r+outfile+'"'+filepath+filename+'"')
    return pageend
    
def overlying(picspath,filename,imgnumlist,lying):
    #TODO lying is about the overlying type
    
    for i in range(0,len(imgnumlist)-1):
        if i==0:
            imageall=Image.open(picspath+filename+'-'+str(imgnumlist[0])+'.tiff')
            continue
        else:
            imgtmp=Image.open(picspath+filename+'-'+str(imgnumlist[i])+'.tiff')
            imageall=ImageChops.darker(imgtmp,imageall)
            imgtmp=None
            continue
    return imageall


def centralizepic(image):
    None

def cropblank(image):

    wlist=generalscan.rawscan(image,'w')
    hlist=generalscan.rawscan(image,'h')
    testedge= generalscan.edgeboxscan(wlist,hlist)
    
    image=image.transform ((testedge[1][0]-testedge[0][0],testedge[1][1]-testedge[0][1]),Image.EXTENT ,(testedge[0][0],testedge[0][1],testedge[1][0],testedge[1][1]))
    return image
