from tkinter import *

root=Tk()
root.title('Hello World!')
#root.geometry('400x400')
root.iconbitmap('C:/Users/Sam Mallet/Desktop/TKinter/Images/BeachballIcon.ico')

def fakeCommand():
	pass

def hide():
	fileFrame.grid_forget()

def show():
	fileFrame.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

def new():
	hideMenuFrames()
	currentStatus.set('File Status')
	fileFrame.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

def cut():
	hideMenuFrames()
	currentStatus.set('Cut Status')
	editFrame.grid(row=0,column=0,columnspan=2,padx=20,pady=20)

def hideMenuFrames():
	editFrame.grid_forget()
	fileFrame.grid_forget()

# define a menu
myMenu = Menu(root)
root.config(menu=myMenu)

# create menu items
fileMenu = Menu(myMenu)
myMenu.add_cascade(label='File', menu=fileMenu) # this is like .pack()
fileMenu.add_command(label='New', command=new) 
# what drops down when you click the menu
fileMenu.add_separator() # puts a separator between commands
fileMenu.add_command(label='Exit', command=root.quit) # quits the program

# create another submenu edit
editMenu = Menu(myMenu)
myMenu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=fakeCommand)
editMenu.add_command(label='Paste', command=fakeCommand)

'''
showButton = Button(root, text='Show', command=show)
hideButton = Button(root, text='Hide', command=hide)

showButton.grid(row=0, column=0)
hideButton.grid(row=0, column=1)
'''

# file menu frame
fileFrame = Frame(root, width=200, height=200, bd=5, bg='blue', relief='sunken')
# bd = border
#fileFrame.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

fileLabel = Label(fileFrame, text='File Frame', font=('Helvetica', 20))
fileLabel.pack(padx=20,pady=20)

# edit menu frame
editFrame = Frame(root, width=200, height=200, bd=5, bg='blue', relief='sunken')
# bd = border
#editFrame.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

editLabel = Label(editFrame, text='Cut Frame', font=('Helvetica', 20))
editLabel.pack(padx=20,pady=20)
myButton = Button(editFrame, text='hi').pack()

# status bar

currentStatus=StringVar() # becomes a funtion
currentStatus.set('Waiting')

myStatus = Label(root, textvariable=currentStatus, bd=2, 
				relief='sunken', width=56, anchor=E) 
				# needs to be text variable with StringVar()
myStatus.grid(row=2, column=0)









root.mainloop()