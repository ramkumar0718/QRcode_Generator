import pyqrcode	
import tkinter 
from tkinter import *
from PIL import ImageTk, Image

root = tkinter.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Qrcode Generator")

# Qrcode Image
my_pic = Image.open("qrcode.PNG")
resized = my_pic.resize((80, 80), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized)
my_pic = ImageTk.PhotoImage(file="qrcode.png")
my_label = Label(root, image=new_pic)
my_label.place(x= 50, y = 15)

tkinter.Label(root, text ='Qrcode Generator:', font ='arial 20 bold').place(x= 140, y = 35)
# Input Link and Size
link = tkinter.StringVar() 
size = tkinter.IntVar()
tkinter.Label(root, text ='Paste url and input size below:', font ='arial 15 bold').place(x= 100, y = 115)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 15, y = 160)
size_enter = tkinter.Entry(root, width = 3, textvariable = size).place(x = 458, y = 160)

def Qrcode_Generator():
    qrcode = pyqrcode.create(str(link.get()))
    qrcode.svg('qrcode.svg', scale = int(size.get()))
    tkinter.Label(root, fg="green", text ='Sucessfully Createed !', font ='arial 16').place(x= 140, y = 260)

tkinter.Button(root, text ='Create', font ='arial 15 bold',padx = 2, command = Qrcode_Generator).place(x=205, y = 200)
tkinter.Label()
root.mainloop() 
