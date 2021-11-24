from tkinter import *

root = Tk()
root.title('HelloWorld!')
root.geometry('400x400')
root.iconbitmap('C:/Users/Sam Mallet/Desktop/Tkinter/Images/BeachBallIcon.ico')

def radio():
	if v.get()=='one':
		myLabel = Label(root, text='You Clicked Radio Button One!')
	else:
		myLabel = Label(root, text='You Clicked Radio Button Two!')
	#myLabel = Label(root, text=v.get())
	myLabel.pack(pady=10)

# radio buttons
#v = IntVar() # tkinter varible that can be updated in real time
# so its actually an object
# if checked v=1 otherwise v=0

'''
rButton1 = Radiobutton(root, text='One', variable=v, value=1).pack()
rButton2 = Radiobutton(root, text='Two', variable=v, value=2).pack()
'''

v = StringVar()
v.set('one') # can also just set is to None

rButton1 = Radiobutton(root, text='One', variable=v, value='one').pack()
rButton2 = Radiobutton(root, text='Two', variable=v, value='two').pack()

myButton = Button(root, text='Click Me', command=radio)
myButton.pack(pady=20)

root.mainloop()