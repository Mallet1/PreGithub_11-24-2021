import os
def folderSize():
    totalSize=0

    print('Enter the folder you want the total size of:')
    folder=str(input())
    for filename in os.listdir(folder):
        #if not os.path.isfile(os.path.join(folder, filename)):
        #    continue
        totalSize=totalSize+os.path.getsize(os.path.join(folder, filename))
    print('Total size of files in the folder in bytes: '+str(totalSize))

def fileInFolder():
    totalSize=0
    
    print('Enter the path of your folder here:')
    folder=str(input())
    
    print('Enter file in the folder here:')
    file=str(input())
    
    totalSize=os.path.getsize(os.path.join(folder, file))
    print('Total size in bytes: '+str(totalSize))

def PythonFilesSize():
    totalSize=0
    
    for filename in os.listdir('C:\\Users\\Sam Mallet\\Desktop\\Python Files'):
        if not os.path.isfile(os.path.join('C:\\Users\\Sam Mallet\\Desktop\\Python Files', filename)):
            continue
        totalSize=totalSize+os.path.getsize(os.path.join('C:\\Users\\Sam Mallet\\Desktop\\Python Files', filename))
    print('Total size of Python Files in bytes: '+str(totalSize))
    
print('Size of folder or file in folder?(1=folder 2=file)')
spam=int(input())

if(spam==1):
    folderSize()
else:
    fileInFolder()
