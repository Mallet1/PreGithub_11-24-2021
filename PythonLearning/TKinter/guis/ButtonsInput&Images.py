from tkinter import *
from PIL import ImageTk, Image

root=Tk()

root.title('Pack Vs. Grid')
root.geometry('400x600')
root.iconbitmap('C:/Users/Sam Mallet/Desktop/TKinter/Images/BeachballIcon.ico')
# creates the icon for the window

# create clicked function

def clicked():
	myLabel2=Label(root, text='You clicked the button!').pack()

def add():
	global newLabel
	newLabel=Label(root, text='hello '+e.get())
	newLabel.pack()

def hide():
	newLabel.pack_forget() # it temporarily removes it
	#newLabel.destroy() # will permanently remove it
	# can also use grid_

def show():
	newLabel.pack()

# add images

myImage= ImageTk.PhotoImage(Image.open('C:/Users/Sam Mallet/Desktop/Automated Python/Rocket Pics/RocketIcon.png'))
imageLabel=Label(image=myImage)
imageLabel.pack()


# create labels and buttons

myButton = Button(root, text='Click Me!', command=clicked)
myButton.pack(pady=20)

hide = Button(root, text='Hide', command=hide)
hide.pack(pady=20)

show = Button(root, text='Show', command=show)
show.pack(pady=20)

myLabel = Label(root, text='Enter your name', relief='sunken')
myLabel.pack()

#things = 2
#myButton2 = Button(root, text='Button2',command=lambda: clicked2(things)).pack()
# lambda to pass parameters


# entry widget

e = Entry(root, font=('Helvetica',20))
e.pack(pady=20)
addButton = Button(root, text='print words',command=add)
addButton.pack(pady=20)








root.mainloop()
