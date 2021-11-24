from tkinter import *

root = Tk()
root.title('HelloWorld!')
root.geometry('400x400')
root.iconbitmap('C:/Users/Sam Mallet/Desktop/Tkinter/Images/BeachBallIcon.ico')

def toppings():
	pizzaToppings=[v.get(),v2.get()]
	myLabel = Label(root, text='You ordered '+', '.join(pizzaToppings))
	myLabel.pack(pady=10)

	#myLabel = Label(root, text=v.get())
	#myLabel.pack(pady=10)

# check boxes

v = StringVar() # constantly updating variable (object)
# v is set to myCheck so when it is check v=pepperoni and off v=no_pepperoni

myCheck = Checkbutton(root, text='Pepperoni', variable=v, onvalue='pepperoni', offvalue='no pepperoni')
# onvalue when checked offvalue when unchecked
myCheck.deselect() # deselects the button
myCheck.pack()

v2=StringVar()
myCheck = Checkbutton(root, text='Sausage', variable=v2, onvalue='sausage', offvalue='no sausage')
myCheck.deselect()
myCheck.pack()

myButton = Button(root, text='Select Toppings', command=toppings).pack(pady=10)

root.mainloop()