from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

root = Tk()
root.title('TicTacToe')
root.geometry('200x110')
root.iconbitmap('C:\\Users\\Sam Mallet\\Desktop\\Tkinter\\Images\\BeachBallIcon.ico')

menuFrame = Frame(root)
boardFrame = Frame(root)
playerXTurn = Button(root)
playerOTurn = Button(root)
placements = [['' for x in range(3)] for y in range(3)] # shows the status of the buttons

tacButtons = [[None for x in range(3)] for y in range(3)] # saves the button objects

turn=0 # saves whos turn it is

checkBoardCount = False # checks if board has been set yet

def select():
	root.geometry('285x305')
	global turn
	if chooseCombo.get() == 'O':
		turn+=1
	setBoard()

def changeTurn():
	playerXTurn.pack_forget()
	playerOTurn.pack_forget()
	if(turn%2==0):
		playerXTurn.pack()
	else:
		playerOTurn.pack()

def checkTie():
	return(placements[0][0]!='' and
		placements[0][1]!='' and
		placements[0][2]!='' and
		placements[1][0]!='' and
		placements[1][1]!='' and
		placements[1][2]!='' and
		placements[2][0]!='' and
		placements[2][1]!='' and
		placements[2][2]!='')

def checkWin(player):
	return((placements[0][0]==player and placements[0][1]==player and placements[0][2]==player) or
		(placements[1][0]==player and placements[1][1]==player and placements[1][2]==player) or
		(placements[2][0]==player and placements[2][1]==player and placements[2][2]==player) or
		(placements[0][0]==player and placements[1][0]==player and placements[2][0]==player) or
		(placements[0][1]==player and placements[1][1]==player and placements[2][1]==player) or
		(placements[0][2]==player and placements[1][2]==player and placements[2][2]==player) or
		(placements[0][0]==player and placements[1][1]==player and placements[2][2]==player) or
		(placements[0][2]==player and placements[1][1]==player and placements[2][0]==player))

def disable():
	for i in range(len(tacButtons)): # loop through rows
		for k in range(len(tacButtons[0])): # loop through columns
			if tacButtons[i][k]['state'] != DISABLED:
				tacButtons[i][k] = Button(boardFrame,state=DISABLED,relief='sunken',height=2,width=5,bd=5,font=('Helvetica',20))

def place(row,column):
	global turn
	
	if turn%2==0:
		placements[row][column]='X'
		if(checkWin('X')):
			win = messagebox.showinfo('WINNER!', 'X Wins!')
			disable()
		elif(checkTie()):
			tie = messagebox.showinfo('thats boring', 'Tied Game!')
			disable()
		tacButtons[row][column] = Button(boardFrame,text='X',state=DISABLED,relief='sunken',height=2,width=5,font=('Helvetica',20))
	else:
		placements[row][column]='O'
		if(checkWin('O')):
			win = messagebox.showinfo('WINNER!', 'O Wins!')
			disable()
		elif(checkTie()):
			tie = messagebox.showinfo('thats boring', 'Tied Game!')
			disable()
		tacButtons[row][column] = Button(boardFrame,text='O',state=DISABLED,relief='sunken',height=2,width=5,font=('Helvetica',20))

	turn+=1
		
	setBoard()

def hideFrame():
	menuFrame.pack_forget()
	boardFrame.pack_forget()

def setBoard():
	hideFrame()
	changeTurn()
	global checkBoardCount
	
	boardFrame.pack(fill='both', expand=1) # creates frame for tictactoe board

	if checkBoardCount == False:
		tacButtons[0][0]=Button(boardFrame,text='',command=lambda:place(0,0),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[0][1]=Button(boardFrame,text='',command=lambda:place(0,1),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[0][2]=Button(boardFrame,text='',command=lambda:place(0,2),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[1][0]=Button(boardFrame,text='',command=lambda:place(1,0),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[1][1]=Button(boardFrame,text='',command=lambda:place(1,1),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[1][2]=Button(boardFrame,text='',command=lambda:place(1,2),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[2][0]=Button(boardFrame,text='',command=lambda:place(2,0),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[2][1]=Button(boardFrame,text='',command=lambda:place(2,1),height=2,width=5,bd=5,font=('Helvetica',20))
		tacButtons[2][2]=Button(boardFrame,text='',command=lambda:place(2,2),height=2,width=5,bd=5,font=('Helvetica',20))
		checkBoardCount=True # creates the original board

	for i in range(len(tacButtons)): # loop through rows
		for k in range(len(tacButtons[0])): # loop through columns
			#if checkBoardCount == False:
			#	tacButtons[i][k]=Button(boardFrame,text=placements[i][k],command=lambda:place(int(i),int(k)),height=2,width=5,font=('Helvetica',20))
			tacButtons[i][k].grid(row=i,column=k)

menuFrame = Frame(root, width=200, height=200, bd=5, bg='yellow',relief='raised')
menuFrame.pack(fill='both', expand=1)

# XorO combo box
XorO = ['X','O']

chooseCombo = ttk.Combobox(menuFrame, value=XorO) # ttk widget
chooseCombo.current(None) # default value based on options list
chooseCombo.pack(padx=5,pady=5)

confirmButton = Button(menuFrame, text='Confirm', command=select)
confirmButton.pack(pady=5, side = BOTTOM)

boardFrame = Frame(root, width=200, height=200, relief='raised')

playerXTurn = Button(root, text='Player X Turn',state='disabled')
playerOTurn = Button(root, text='Player O Turn',state='disabled')


root.mainloop()