import os
def findFile(file):
    for folderName,subfolders,filenames in os.walk('C:\\'):
        for x in filenames:
            if(file.lower() in x.lower()):
                print('The path for '+x+' is '+os.path.dirname(folderName)+os.sep+os.path.basename(folderName))
                print()

def findFolder(folder):
    for folderName,subfolders,filenames in os.walk('C:\\'):
        for x in subfolders:
            if(folder.lower() in x.lower()):
                print('The path for '+x+' is '+os.path.dirname(folderName)+os.sep+os.path.basename(folderName))
                print()

stop=''
while stop=='':
    print('folder or file?')
    which=str(input())

    if(which=='file'):
        print('What file would you like to find in the c drive?')
        theFile = str(input())
        findFile(theFile)
    elif(which=='folder'):
        print('What folder would you like to find in the c drive?')
        theFolder = str(input())
        findFolder(theFolder)
    print('press enter to continue and 0 to end')
    stop=input()
