from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.title('HelloWorld!')
root.geometry('400x400')
root.iconbitmap('C:\\Users\\Sam Mallet\\Desktop\\Tkinter\\Images\\BeachBallIcon.ico')

def openImage():
	# open dialog box
	root.filename = filedialog.askopenfilename(initialdir='C:\\Users\\Sam Mallet\\Desktop\\TKinter\\Images', title='Open An Image File', 
		filetypes=( ('ICO File', '*.ico'), ('PNG File', '*.png'), ('All Files', '*.*') )) # could leave only all files and wouldn't change
	# root.filename now returns whatever file path we click on
	# open filedialog with the askopenfilename function
	# filetypes states the filetypes that are allowed to be passed

	#myLabel = Label(root, text=root.filename).pack(pady=10)

	global myImage

	# open the image you click

	myImage= ImageTk.PhotoImage(Image.open(root.filename))
	imageLabel=Label(image=myImage)
	imageLabel.pack(pady=10)



myButton = Button(root, text='Open Image', command=openImage).pack(pady=10)

root.mainloop()