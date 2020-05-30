import sys	from tkinter import*
import os	def NewFile():
def file_read_from_tail(fname,lines):	  print("New File!")
    bufsize=8192	def OpenFile():
    fsize=os.stat(fname).st_size	  print("Open File!")
    iter=0	def ExitFile():
    with open(fname) as f:	  print("Exit File!")
        if bufsize>fsize:	def TextInsert():
            bufsize=fsize-1	  print("Text Insert!")
            data =[]	def PictureInsert():
            while True:	  print("Picture Insert!")
                iter+=1	def About():
                f.seek(fsize-bufsize*iter)	  print("This is a simple example of a menu")
                data.extend(f.readlines())	root = Tk()
                if len(data)>=lines or f.tell()==0:	menu = Menu(root)
                    print(''.join(data[-lines:]))	root.config(menu=menu)
                    break	filemenu=Menu(menu)
file_read_from_tail('text.txt',2)
