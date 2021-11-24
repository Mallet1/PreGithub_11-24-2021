def hello(name):
    print('Hello '+name)

def plusOne(number):
    return number+1
    

hello('hi')
hello('sam')
newNum=plusOne(5)
print(newNum)

#Functions default to the None value if it doesn't have a return statement

print('Hello',end='') #Doesn't give new line
print('World')

print('cat', 'dog',  'mouse', sep='ABC')#Separates each word with ABC
