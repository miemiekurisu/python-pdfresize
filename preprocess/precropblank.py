import Image
import os

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
    
def extracttoimg(file):
    None

def cropblank(image):
    None

