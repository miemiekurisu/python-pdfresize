ActivePython 2.7.2.5 (ActiveState Software Inc.) based on
Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pyPDF

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pyPDF
ImportError: No module named pyPDF
>>> from pyPdf import PdfFileWriter, PdfFileReader
>>> import pyPdf
>>> import Image
>>>  import os
 
  File "<pyshell#4>", line 1
    import os
   ^
IndentationError: unexpected indent
>>> import os
>>> pdf1 = PdfFileReader('D:\\1.pdf')

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pdf1 = PdfFileReader('D:\\1.pdf')
  File "C:\Python27A\lib\site-packages\pyPdf\pdf.py", line 374, in __init__
    self.read(stream)
  File "C:\Python27A\lib\site-packages\pyPdf\pdf.py", line 702, in read
    stream.seek(-1, 2)
AttributeError: 'str' object has no attribute 'seek'
>>> input1 = PdfFileReader(file("D:\1.pdf", "rb"))

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    input1 = PdfFileReader(file("D:\1.pdf", "rb"))
IOError: [Errno 22] invalid mode ('rb') or filename: 'D:\x01.pdf'
>>> input1 = PdfFileReader(file("D:\\1.pdf", "rb"))
>>> input1.documentInfo
{'/Subject': u'Mathematics computer science', '/Author': u'Knuth Graham Patashnik - Simon Plouffe', '/Producer': 'Acrobat 4.0 Import Plug-in for Macintosh\x00', '/Creator': 'Acrobat 4.0 Capture Plug-in for Windows\x00', '/ModDate': u"D:20010330013054-05'00'", '/Title': u'Concrete Mathematics', '/CreationDate': u"D:20000831223445-04'00'"}
>>> pageCount=input.getNumPages()

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pageCount=input.getNumPages()
AttributeError: 'builtin_function_or_method' object has no attribute 'getNumPages'
>>> pageCount=input1.getNumPages()
>>> print pageCount
640
>>> input1.close()

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    input1.close()
AttributeError: 'PdfFileReader' object has no attribute 'close'
>>> img=Image.open('D:\\count2.png')

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    img=Image.open('D:\\count2.png')
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1952, in open
    fp = __builtin__.open(fp, "rb")
IOError: [Errno 2] No such file or directory: 'D:\\count2.png'
>>> IOError: [Errno 2] No such file or directory: 'D:\\count2.png'
SyntaxError: invalid syntax
>>> img=Image.open('D:\\cover2.png')
>>> img.size
(1717, 2225)
>>> w,h = img.size
>>> img.transform((w,1),Image.EXTENT,(0,0,w,1))
<Image.Image image mode=L size=1717x1 at 0x28857D8>
>>> split1 = img.transform((w,1),Image.EXTENT,(0,0,w,1))
>>> split1
<Image.Image image mode=L size=1717x1 at 0x284FDA0>
>>> pix = split1.load()
>>> pix
<PixelAccess object at 0x0161D100>
>>> split1.show()
>>> split1.info
{}
>>> split1 = img.transform((w,1),Image.EXTENT,(0,0,w,1))
>>> split1.save ('d:\\test1.png')
>>> split1.getdata()
<ImagingCore object at 0x0161D200>
>>> d=split1.getdata()
>>> d
<ImagingCore object at 0x0161D200>
>>> list(d)
[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
>>> l=list(d)
>>> l.size

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    l.size
AttributeError: 'list' object has no attribute 'size'
>>> l.size()

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    l.size()
AttributeError: 'list' object has no attribute 'size'
>>> l.count
<built-in method count of list object at 0x0284FDA0>
>>> l.count()

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l.count()
TypeError: count() takes exactly one argument (0 given)
>>> ================================ RESTART ================================
>>> import Image
>>> import pyPdf
>>> import os
>>> import subprocess
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r150 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r50 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r80 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r120 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r150 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=59 -dLastPage=59 -r150 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=59 -dLastPage=59 -r200 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> img = Image.open ('d:\\cover2.png')
>>> w,h = img.size
>>> one = img.transform ((w,1),Image.EXTENT ,(0,100,w,1))
>>> one.save('d:\\one.png')
>>> one = img.transform ((w,30),Image.EXTENT ,(0,100,w,30))
>>> one.save('d:\\one.png')
>>> os.system('gswin32c.exe -q -sDEVICE=bmpgray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r150 -sOutputFile="D:\\cover2.bmp" "D:\\1.pdf"')
0
>>> p=[]
>>> for i in h:
	p.append(list(img.transform ((w,1),Image.EXTENT ,(0,i,w,1))))

	

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    for i in h:
TypeError: 'int' object is not iterable
>>> for i in h:
	p.append(list(img.transform ((w,1),Image.EXTENT ,(0,i,w,1)).getdata()))

	

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    for i in h:
TypeError: 'int' object is not iterable
>>> for i in h:
	spl = img.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	spl1 = list(spl.getdata())
	p.append(spl1)

	

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    for i in h:
TypeError: 'int' object is not iterable
>>> while i <= h:
	spl = img.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	spl1 = list(spl.getdata())
	p.append(spl1)

	

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    while i <= h:
NameError: name 'i' is not defined
>>> i=0
>>> i=1
>>> for i in h:
	spl = img.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	spl1 = list(spl.getdata())
	p.append(spl1)

	

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    for i in h:
TypeError: 'int' object is not iterable
>>> while i <=h:
	spl = img.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	spl1 = list(spl.getdata())
	p.append(spl1)

	

Traceback (most recent call last):
>>> ================================ RESTART ================================
>>> while i <=h:
	spl = img.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	spl1 = list(spl.getdata())

	

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    while i <=h:
NameError: name 'i' is not defined

>>> i=1
>>> while i <=h:
	spl = img.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	spl1 = list(spl.getdata())

	

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    while i <=h:
NameError: name 'h' is not defined
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r300 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r300 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
NameError: name 'os' is not defined
>>> import os
>>> import Image
>>> import subprocess
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r200 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=1 -dLastPage=1 -r200 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> os.system('gswin32c.exe -q -sDEVICE=pnggray -dBATCH -dNOPAUSE -dFirstPage=56 -dLastPage=56 -r200 -sOutputFile="D:\\cover2.png" "D:\\1.pdf"')
0
>>> img = Image.open('D:\\cover2.png')
>>> w,h = img.size
>>> imgl=img.convert('l')

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    imgl=img.convert('l')
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 702, in convert
    im = im.convert(mode, dither)
ValueError: conversion from L to l not supported
>>> imgt=img.transpose(Image.FLIP_TOP_BOTTOM)
>>> imgt.save('D:\\imgt.png')
>>> imgl=img.convert('1')
>>> imgt.save('D:\\imgt.png')
>>> img = Image.open('D:\\cover2.png')
>>> w,h = img.size
>>> imgl=img.convert('l')

Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    imgl=img.convert('l')
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 702, in convert
    im = im.convert(mode, dither)
ValueError: conversion from L to l not supported
>>> imgl=img.convert('1')
>>> imgt.save('D:\\imgt.png')
>>> imgl.save('D:\\imgt.png')
>>> import ImageFilter
>>> imge = imgl.filter (ImageFilter.FIND_EDGES)

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    imge = imgl.filter (ImageFilter.FIND_EDGES)
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 813, in filter
    return self._new(filter.filter(self.im))
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\ImageFilter.py", line 55, in filter
    return apply(image.filter, self.filterargs)
ValueError: image has wrong mode
>>> imge = img.filter (ImageFilter.FIND_EDGES)
>>> imge.save('D:\\imge.png')
>>> imgr = ImageChops.invert(img)

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    imgr = ImageChops.invert(img)
NameError: name 'ImageChops' is not defined
>>> import ImageChops
>>> imgr = ImageChops.invert(img)
>>> imgr.save('D:\\imgr.png')
>>> imgr1=imgr.transform ((w,1),Image.EXTENT ,(0,0,w,1))
>>> imgr1.show()
>>> list(imgr1.getdata())
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> l1 = list(imgr1.getdata())
>>> 0in l1
True
>>> 255 in l1
False
>>> img.show()
>>> i=1
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		return 0
	
SyntaxError: 'return' outside function
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'

	

Traceback (most recent call last):
  File "<pyshell#118>", line 2, in <module>
    img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1609, in transform
    im = new(self.mode, size, None)
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1755, in new
    return Image()._new(core.new(mode, size))
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 462, in _new
    new.im = im
KeyboardInterrupt
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		
KeyboardInterrupt
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print 'find edge'
KeyboardInterrupt
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
	else:
		
  File "<pyshell#123>", line 4
    else:
       ^
IndentationError: expected an indented block
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		i++
	else: continue
	
SyntaxError: invalid syntax
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		i++
		print 'find edge'	
	else: continue
	
SyntaxError: invalid syntax
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		i++

		
SyntaxError: invalid syntax
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		i+=i
		print 'find edge'
	else: continue
	
KeyboardInterrupt
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		i+=i
		print 'find edge'
	else:
		i+=i
		continue

	
find edge
find edge
find edge
find edge
find edge
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		i+=i
		print i
		print 'find edge'
	else:
		print i
		i+=i
		continue

	
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		i+=i
		print i
		print 'find edge'
	else:
		print i
		i+=i
		continue

	
>>> while i < h:
	img1=img.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		i+=i
		print 'find edge'
	else:
		i+=i
		continue

	
>>> print i
4096
>>> img.size
(1722, 2231)
>>> cover2 = Image.open ('D:\\cover2.png')
>>> coverbw = cover2.convert (1)

Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    coverbw = cover2.convert (1)
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 697, in convert
    im = self.im.convert(mode, dither)
TypeError: must be string, not int
>>> coverbw = cover2.convert ('1')
>>> i=0
>>> i=1
>>> w,h = coverbw.size
>>> while i < h:
	img1=coverbw.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
	else:
		i+=i
		continue

	
find edge
128
find edge
256
find edge
512
find edge
1024
find edge
2048
>>> while i < h:
	img1=coverbw.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		break
	else:
		i+=i
		continue

	
>>> i=1
>>> while i < h:
	img1=coverbw.transform ((w,i),Image.EXTENT ,(i-1,0,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		break
	else:
		i+=i
		continue

	
find edge
128
>>> imgcorp = coverbw.transform ((w,128),Image.EXTENT ,(0,0,w,128))
>>> imgcorp.save('D:\\imgcorp.png')
>>> imgcorp = coverbw.transform ((w,256),Image.EXTENT ,(0,0,w,256))
>>> imgcorp.save('D:\\imgcorp.png')
>>> imgcorp = coverbw.transform ((w,1024),Image.EXTENT ,(0,0,w,1024))
>>> imgcorp.save('D:\\imgcorp.png')
>>> i=0
>>> i=1
>>> while i < h:
	img1=coverbw.transform ((w,i),Image.EXTENT ,(0,i-1,w,i))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		break
	else:
		i+=i
		continue

	
find edge
256
>>> i=0
>>> i=1
>>> while i < h:
	img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i-1,w,1))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		break
	else:
		i+=i
		continue

	
find edge
512
>>>  imgcorp = coverbw.transform ((w,1),Image.EXTENT ,(0,512,w,1))
 
  File "<pyshell#168>", line 1
    imgcorp = coverbw.transform ((w,1),Image.EXTENT ,(0,512,w,1))
   ^
IndentationError: unexpected indent
>>> imgcorp = coverbw.transform ((w,1),Image.EXTENT ,(0,512,w,1))
>>> imgcorp.save('D:\\imgcorp.png')
>>> list(imgcorp.getdata())
[255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 0, 0, 0, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
>>> while i < h:
	img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i-1,w,1))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		break
	else:
		i+=i
		continue

	
find edge
1024
>>> i=1
>>> i=0
>>> while i < h:
	img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		
	else:
		i+=i
		continue

	

Traceback (most recent call last):
  File "<pyshell#177>", line 2, in <module>
    img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i,w,1))
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1615, in transform
    im.__transformer((0, 0)+size, self, method, data, resample, fill)
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1624, in __transformer
    w = box[2]-box[0]
KeyboardInterrupt

>>> while i < h:
	img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
	else:
		i+=i
		continue

	

Traceback (most recent call last):
  File "<pyshell#179>", line 2, in <module>
    img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i,w,1))
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1609, in transform
    im = new(self.mode, size, None)
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1755, in new
    return Image()._new(core.new(mode, size))
KeyboardInterrupt
>>> while i < h:
	img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i-1,w,1))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		break
	else:
		i+=i
		continue

	

Traceback (most recent call last):
  File "<pyshell#181>", line 2, in <module>
    img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i-1,w,1))
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1609, in transform
    im = new(self.mode, size, None)
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 1755, in new
    return Image()._new(core.new(mode, size))
  File "C:\Python27A\lib\site-packages\pil-1.1.7-py2.7-win32.egg\Image.py", line 469, in _new
    new.info = self.info.copy()
KeyboardInterrupt
>>> print i
0
>>> i=0
>>> while i < h:
	img1=coverbw.transform ((w,1),Image.EXTENT ,(0,i,w,1))
	if 0 in list(img1.getdata()):
		print 'find edge'
		print i
		i+=i
		break
	else:
		i+=i
		continue

	


