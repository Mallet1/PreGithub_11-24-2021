from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title('HelloWorld!')
root.geometry('400x400')
root.iconbitmap('C:\\Users\\Sam Mallet\\Desktop\\Tkinter\\Images\\BeachBallIcon.ico')

def color():
	myColor = colorchooser.askcolor()[1] # [0] gets rgb data [1] gets hex code
	# opens the color chooser and returns a list of tuples with rgb data of your choice
	myLabel = Label(root, text=myColor).pack()
	myLabel2 = Label(root, text='You Picked A Color!!', font=('Helvetica', 32), bg=myColor).pack()

myButton = Button(root, text='Pick A Color', command=color).pack()













root.mainloop()