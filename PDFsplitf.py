ActivePython 2.7.2.5 (ActiveState Software Inc.) based on
Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import Image
>>> import os
>>> im  = Image.op

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    im  = Image.op
AttributeError: 'module' object has no attribute 'op'
>>> im  = Image.open("D:\\cover.png")
>>> im.size
(2575, 3338)
>>> w,h=im.size
>>> w
2575
>>> h
3338
>>> import subprocess
>>> args = ['gswin32c.exe','-q', '-sDEVICE=pnggray','-dBATCH', '-dNOPAUSE' ,'-dFirstPage=1', '-dLastPage=1', '-r150', '-sOutputFile="D:\\cover2.png"', '"D:\\1.pdf"']
>>> output = Popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    output = Popen( args, stdout = sys.stdout, stderr = sys.stderr )
NameError: name 'Popen' is not defined
>>> output = popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    output = popen( args, stdout = sys.stdout, stderr = sys.stderr )
NameError: name 'popen' is not defined
>>> output = subprocess.Po( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    output = subprocess.Po( args, stdout = sys.stdout, stderr = sys.stderr )
AttributeError: 'module' object has no attribute 'Po'
>>> output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )
NameError: name 'sys' is not defined
>>> output = subprocess.Popen( args )
>>> import sys
>>> output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )
  File "C:\Python27A\lib\subprocess.py", line 672, in __init__
    errread, errwrite) = self._get_handles(stdin, stdout, stderr)
  File "C:\Python27A\lib\subprocess.py", line 796, in _get_handles
    c2pwrite = msvcrt.get_osfhandle(stdout.fileno())
AttributeError: fileno
>>> args = ['gswin32c.exe','-q', '-sDEVICE=pnggray','-dBATCH', '-dNOPAUSE' ,'-dFirstPage=1', '-dLastPage=1', '-r150', '-sOutputFile="D:\cover2.png"', '"D:\1.pdf"']
>>> output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )
  File "C:\Python27A\lib\subprocess.py", line 672, in __init__
    errread, errwrite) = self._get_handles(stdin, stdout, stderr)
  File "C:\Python27A\lib\subprocess.py", line 796, in _get_handles
    c2pwrite = msvcrt.get_osfhandle(stdout.fileno())
AttributeError: fileno
>>> args = ['gswin32c.exe','-q', '-sDEVICE=pnggray','-dBATCH', '-dNOPAUSE' ,'-dFirstPage=1', '-dLastPage=1', '-r150', '-sOutputFile="D:\cover2.png" "D:\1.pdf"']
>>> output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )
  File "C:\Python27A\lib\subprocess.py", line 672, in __init__
    errread, errwrite) = self._get_handles(stdin, stdout, stderr)
  File "C:\Python27A\lib\subprocess.py", line 796, in _get_handles
    c2pwrite = msvcrt.get_osfhandle(stdout.fileno())
AttributeError: fileno
>>> args = ['gswin32c.exe','-q', '-sDEVICE=pnggray','-dBATCH', '-dNOPAUSE' ,'-dFirstPage=1', '-dLastPage=1', '-r150', '-sOutputFile="D:\\cover2.png" "D:\\1.pdf"']
>>> output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )
  File "C:\Python27A\lib\subprocess.py", line 672, in __init__
    errread, errwrite) = self._get_handles(stdin, stdout, stderr)
  File "C:\Python27A\lib\subprocess.py", line 796, in _get_handles
    c2pwrite = msvcrt.get_osfhandle(stdout.fileno())
AttributeError: fileno
>>> args = ['gswin32c.exe','-q', '-sDEVICE=pnggray','-dBATCH', '-dNOPAUSE' ,'-dFirstPage=1', '-dLastPage=1', '-r150', '-sOutputFile=D:\cover2.png D:\1.pdf']
>>> output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    output = subprocess.Popen( args, stdout = sys.stdout, stderr = sys.stderr )
  File "C:\Python27A\lib\subprocess.py", line 672, in __init__
    errread, errwrite) = self._get_handles(stdin, stdout, stderr)
  File "C:\Python27A\lib\subprocess.py", line 796, in _get_handles
    c2pwrite = msvcrt.get_osfhandle(stdout.fileno())
AttributeError: fileno
>>> output = subprocess.Popen( args)
>>> args = ['gswin32c.exe','-q', '-sDEVICE=pnggray','-dBATCH', '-dNOPAUSE' ,'-dFirstPage=1', '-dLastPage=1', '-r150', '-sOutputFile="D:\cover2.png" "D:\1.pdf"']
>>> output = subprocess.Popen( args)
>>> args = ['gswin32c.exe','-q', '-sDEVICE=pnggray','-dBATCH', '-dNOPAUSE' ,'-dFirstPage=1', '-dLastPage=1', '-r150', '-sOutputFile="D:\\cover2.png" "D:\\1.pdf"']
>>> output = subprocess.Popen( args)
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r150 -sOutputFile="D:\cover2.png" "D:\1.pdf"')
1
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r150 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r200 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> 
>>> 
>>> import arcpy

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    import arcpy
ImportError: No module named arcpy
>>> import re
>>> pdfDoc = arcpy.mapping.PDFDocumentOpen('D:\\1.pdf')

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    pdfDoc = arcpy.mapping.PDFDocumentOpen('D:\\1.pdf')
NameError: name 'arcpy' is not defined
>>> import pyPDF

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    import pyPDF
ImportError: No module named pyPDF
>>> 
