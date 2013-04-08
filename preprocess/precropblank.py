import Image
import os

global gspath
global temppath

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

def propertyfile():
    None

def extracttoimg(): #static arg for developing/testing
    if(os.sys.platform=='win32'):
        gspath = 'gswin32c.exe'
        filepath= 'D:\\temp\\'
        flag='\\'
    else:
        gspath = '/usr/local/bin/gs'
        filepath = '/Users/chris/Dev/tmp/'
        flag='/'
    filename = '1.pdf'
    pagerange=[1,670]
    dpi=150
    
    cmdstr1=' -q -sDEVICE=pnggray -dBATCH -dNOPAUSE '
    firstpage = '-dFirstPage='+str(pagerange[0])+' '
    lastpage = '-dLastPage='+str(pagerange[1])+' '
    r = '-r'+str(dpi)+' '
    outfile = '-sOutputFile="'+filepath+filename+'tmp'+flag+filename+'-%d.png" '
    
    if os.path.isdir(filepath+filename+'tmp'): 
        pass 
    else: 
        os.mkdir(filepath+filename+'tmp')
    os.system(gspath+cmdstr1+firstpage+lastpage+r+outfile+'"'+filepath+filename+'"')
    

def cropblank(image):
    None

