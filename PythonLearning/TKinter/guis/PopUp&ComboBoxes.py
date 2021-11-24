from tkinter import *
from tkinter import messagebox # popup
from tkinter import ttk # combobox

root = Tk()
root.title('HelloWorld!')
root.geometry('400x400')
root.iconbitmap('C:/Users/Sam Mallet/Desktop/Tkinter/Images/BeachBallIcon.ico')

# create popup function
def popup():
	response = messagebox.askyesno('Popup Title', 'Look at my popup message!!') # message box wiget
	myLabel = Label(root, text=response).pack(pady=10) # yes = 1 no = 0 for yesno
	# yes = yes no = no for askquestion

	'''
	if response==1:
		myLabel = Label(root, text='You clicked yes!').pack(pady=10)
	else:
		myLabel = Label(root, text='You clicked no!').pack(pady=10)
	'''

def select():
	for i in range(len(options)):
		if(myCombo.get()==options[i]):
			myLabel = Label(root, text='You chose '+options[i]).pack(pady=10)
	# seems like mycombo is its own StringVar() so its constantly updating it's self


	

# popup boxes
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

popButton = Button(root, text='Click To Pop Up!', command=popup)
popButton.pack(pady=20)

# combo boxes

options = [
	'Monday',
	'Tuesday',
	'Wednesday',	
]

myCombo = ttk.Combobox(root, value=options) # ttk widget
myCombo.current(0) # default value based on options list
myCombo.pack(pady=10) 

myButton = Button(root, text='Select', command=select).pack()





root.mainloop()