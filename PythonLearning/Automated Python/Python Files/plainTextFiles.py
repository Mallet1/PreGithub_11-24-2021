# TYPE IN IDLE FOR IT TO WORK

# read mode
helloFile = open('C:\\Users\\Sam Mallet\\asparigus.txt') # Opens file in read mode (can't edit)

content = helloFile.read() # returns a string of the plaintext's contents
print(content)
helloFile.close() # Closes the file

helloFile = open('C:\\Users\\Sam Mallet\\asparigus.txt')
print(helloFile.readlines()) # returns strings in the file as a list

# write/append mode
# write overrides what is already in the file
# append adds to what is already in the file

helloFile = open('C:\\Users\\Sam Mallet\\asparigus.txt','w') # write mode
helloFile = open('C:\\Users\\Sam Mallet\\asparigus.txt', 'a') # append mode
helloFile = open('C:\\Users\\Sam Mallet\\asparigus.txt', 'wb') # write binary mode
helloFile = open('C:\\Users\\Sam Mallet\\asparigus.txt', 'rb') # read binary mode
# if the file doesn't already exist it creates a new blank one

helloFile = open('C:\\Users\\Sam Mallet\\bruh.txt','w')
helloFile.write('Hello!!!!!!') # adds this text to the file and returns the characters you added to it

baconFile = open('bacon.txt','w') # Creats bacon.txt in the cwd
baconFile.write('Bacon is not a vegetable.')

# Shelve is better for storing complex data like lists and dictionaries
import shelve

shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka','Simon','Fat-tail','Cleo'] # like a dictionary
# 'cats' being the key and list after it being the values
shelfFile.close()

shelfFile=shelve.open('mydata')
shelfFile['cats']

list(shelfFile.keys()) # returns the keys
list(shelfFile.values()) # returns the values
