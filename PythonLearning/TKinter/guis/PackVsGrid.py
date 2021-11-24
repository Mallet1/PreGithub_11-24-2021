from tkinter import *

root=Tk()

root.title('Pack Vs. Grid')
root.geometry('400x400')

myLabel = Label(root, text='Hello World!', relief='raised')
myLabel.grid(row=0, column=0, columnspan=2) # top left = 0,0
# can also do rowspan

myLabel2 = Label(root, text='wassup', relief='raised')
myLabel2.grid(row=1, column=0, sticky=W) 
# W = west others just the first letter capitalized

myLabel3 = Label(root, text='Label 3', relief='raised')
myLabel3.grid(row=1, column=1) 
















root.mainloop()