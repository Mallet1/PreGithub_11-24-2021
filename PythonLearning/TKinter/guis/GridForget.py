from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title('HelloWorld!')
root.geometry('400x400')
root.iconbitmap('C:\\Users\\Sam Mallet\\Desktop\\Tkinter\\Images\\BeachBallIcon.ico')

helloLabel = Label(root)
# if you want to forget it every time you use submit() need to declare before

def submit():
	global helloLabel
	helloLabel.grid_forget()
	#clear()
	helloLabel = Label(root, text='Hello ' + e.get())
	helloLabel.grid(row=3,column=0)

def clear():
	helloLabel.grid_forget()
	#helloLabel.destroy()

# forget
myLabel = Label(root, text='Enter Your Name:').grid(row=0,column=0)

e = Entry(root)
e.grid(row=1,column=0)

myButton = Button(root,text='Submit',command=submit).grid(row=2,column=0)

clearButton = Button(root, text='Clear', command=clear).grid(row=2,column=1)

root.mainloop()