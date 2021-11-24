from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('Flashcard App!')
root.geometry('400x400')
root.iconbitmap('C:\\Users\\Sam Mallet\\Desktop\\TKinter\\Images\\BeachBallIcon.ico')

def add():
	hideFrames()
	addFrame.pack(fill='both',expand=1)

def subtract():
	hideFrames()
	subtractFrame.pack(fill='both',expand=1)

def multiply():
	hideFrames()
	multiplyFrame.pack(fill='both',expand=1)

def divide():
	hideFrames()
	divideFrame.pack(fill='both',expand=1)

def hideFrames():
	addFrame.pack_forget()
	subtractFrame.pack_forget()
	multiplyFrame.pack_forget()
	divideFrame.pack_forget()

myMenu=Menu(root)
root.config(menu=myMenu)

mathMenu=Menu(myMenu)
myMenu.add_cascade(label='MathCards', menu=mathMenu)
mathMenu.add_command(label='Add', command=add)
mathMenu.add_command(label='Subtract', command=subtract)
mathMenu.add_command(label='Multiply', command=multiply)
mathMenu.add_command(label='Divide', command=divide)
mathMenu.add_separator()
mathMenu.add_command(label='Exit', command=exit)

# create frames
addFrame = Frame(root, width=400, height=400, bg='blue')
subtractFrame = Frame(root, width=400, height=400, bg='red')
multiplyFrame = Frame(root, width=400, height=400, bg='yellow')
divideFrame = Frame(root, width=400, height=400, bg='green')








root.mainloop()