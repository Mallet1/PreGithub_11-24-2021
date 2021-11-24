spam=42 #Global variable in local scope. Dies when whole program ends

def eggs():
    spam=5 #Local variable in local scope. Destroyed when funtion call is over

def addOne():
    newSpam=spam+1
    return newSpam

def addOneImproved():
    global spam #Defines spam as the global spam variable instead of a new local one
    spam+=1

eggs()

addOneImproved()
print(spam)

h=addOne()
print(h)
