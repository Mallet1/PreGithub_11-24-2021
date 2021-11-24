import os

#print('What file would you like to find in the c drive?')
#file = str(input())

# os.walk returns three variables the folder name the sub folders and the file names
# the for loops just gets them
for folderName,subfolders,filenames in os.walk('C:\\Users\\Sam Mallet\\Desktop\\Testing'):
    print('The folder is '+os.path.basename(folderName))
    print('The subfolders in '+os.path.basename(folderName)+' are: '+str(subfolders))
    print('The filenames in '+os.path.basename(folderName)+' are: '+str(filenames))
    print()

    #if(os.path.basename(folderName)=='Testing'):
    #    print('The subfolders in '+os.path.basename(folderName)+' are: '+str(subfolders))
    #    print('The filenames in '+os.path.basename(folderName)+' are: '+str(filenames))
    #    print()

    #if(file in filenames):
    #    print('The path for '+file+' is '+os.path.dirname(folderName))
    #    print()
# prints every folder and file name in testing

# can be used for many things as you can loop through every thing in a folder
# example renaming every file in a folder that contains a certain string
