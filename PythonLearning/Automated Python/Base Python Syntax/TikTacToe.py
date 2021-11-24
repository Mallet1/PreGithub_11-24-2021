import pprint

def board():
    print(str(theBoard['Top-L'])+'|'+str(theBoard['Top-M'])+'|'+str(theBoard['Top-R']))
    print('-----')
    print(str(theBoard['Mid-L'])+'|'+str(theBoard['Mid-M'])+'|'+str(theBoard['Mid-R']))
    print('-----')
    print(str(theBoard['Bot-L'])+'|'+str(theBoard['Bot-M'])+'|'+str(theBoard['Bot-R']))

def isOpen(pos):
    return theBoard[pos]==isinstance(theBoard[pos],int)

def xMove(move):
    if(move==1 and isOpen(theBoard['Top-L'])):
        theBoard['Top-L']=str('x')

theBoard={'Top-L':1,'Top-M':2,'Top-R':3,
          'Mid-L':4,'Mid-M':5,'Mid-R':6,
          'Bot-L':7,'Bot-M':8,'Bot-R':9,}
XorO=''

print('Hi welcome to tic tac toe')
print('Would u like to be X or O')
XorO=input().upper()
while XorO!='X' and XorO!='O':
    print('Invalid try again')
    XorO=input().upper()

board()
print('Choose the number position of where you want to play')
move=input()
xMove(move)
board()
