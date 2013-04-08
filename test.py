import os 
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

os.system(gspath+cmdstr1+firstpage+lastpage+r+outfile+'"'+filepath+filename+'"')
