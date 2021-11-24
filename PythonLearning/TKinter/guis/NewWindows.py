from tkinter import *
from tkinter import messagebox # popup
from tkinter import ttk # combobox
from PIL import ImageTk, Image
import os

root = Tk()
root.title('HelloWorld!')
root.geometry('400x400')
root.iconbitmap('C:/Users/Sam Mallet/Desktop/Tkinter/Images/BeachBallIcon.ico')

def newWindow():
	new = Toplevel()
	new.title('New Window')
	new.geometry('400x400')
	new.iconbitmap('C:/Users/Sam Mallet/Desktop/Tkinter/Images/BeachBallIcon.ico')

	#global myImg

	myLabel = Label(new, text='2nd window').pack(pady=20)

	os.chdir('C:\\Users\\Sam Mallet\\Desktop\\TKinter\\Images')
	myImg = ImageTk.PhotoImage(Image.open('BeachBallIcon.ico'))
	imgLabel = Label(new, image=myImg)
	imgLabel.pack(pady=5)


	destroyButton = Button(new, text='Quit', command=new.destroy) # .destroy destroys window
	destroyButton.pack(pady=5)

	#hideButton = Button(new, text='Hide Main Window', command=root.iconify) # .iconify minimizes window
	#showButton = Button(new, text='Show Main Window', command=root.deiconify) # .deiconify shows window

	# withdraw original window
	hideButton = Button(new, text='Hide Main Window', command=root.withdraw) # .withdraw hides window
	showButton = Button(new, text='Show Main Window', command=root.deiconify)

	killOriginal = Button(new, text='Quit Original', command=root.destroy).pack()
	hideButton.pack()
	showButton.pack()


	new.mainloop() # independent window without a parent
	# images don't work without the main loop unless you make the image global


# create new windows
myButton = Button(root, text='2nd Window', command=newWindow).pack(pady=10)




root.mainloop()