from tkinter import *

# to run a program type python then the file name in git bash
# to activate virtual environment source virt/Scripts/activate
# to deactivate virtual environment type deactivate

root = Tk() # creating a root instance of Tk
root.title('Hello World!')
root.geometry('700x700') # dimensions

myLabel = Label(root, text='Hello World!', fg='white', bg='black') 
# (window, text='', fgcolor, bgcolor)
myLabel.pack() # puts things in nice spots automatically

myLabel2 = Label(root, text='wassup', font=('Helvtica', 32)) 
# (font, size) 
myLabel2.pack()

myLabel2 = Label(root, text='sup', relief='sunken', height=20, width=20) 
# 'raised' 'groove' 'ridge' also work 
myLabel2.pack()

myLabel2 = Label(root, text='disabled', state='disabled') 
# 'normal'
myLabel2.pack(pady=50) # pushes it down 50 pixels




root.mainloop() # the main loop to create the gui