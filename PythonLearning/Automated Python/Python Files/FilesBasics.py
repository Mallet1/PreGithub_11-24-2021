import os

spam=os.path.join('folder1', 'folder2', 'folder3', 'file.png') # Creates path to png file
print(spam)
print(r''+os.sep) # Shows separator for your pc

print('cwd: '+os.getcwd()) # Current working directory (cwd)

# print(os.chdir('')) # Can be used to change the cwd

# Absolute file path (always begins with the root folder):
# c:\folder1\folder2\spam.png

# Relative file path (Assumes it can be found in the cwd):
# spam.png
# \folder1\folder2\spam.png assumes the cwd then goes into more folders in the cwd

# A . means cwd in relative file paths / "this folder"
# A .. means parent folder in relative file paths / "the parent folder"

print('\n'+str(os.path.abspath('spam.png'))) # returns the absolute path
print('\n'+str(os.path.abspath('..\\..\\spam.png'))) # takes out last 2 folders

print('isabs: '+str(os.path.isabs('spam.png'))) # returns true if it is an abs path

print('relpath: '+str(os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1'))) # given c:\\folder1 is cwd
# .relpath gives the relative path between 2 paths you give it

print()
print('dirname: '+str(os.path.dirname('c:\\folder1\\folder2\\spam.png'))) # returns the directory part
print('basename: '+str(os.path.basename('c:\\folder1\\folder2\\spam.png'))) # returns last part

print('\nexists: '+str(os.path.exists('c:\\windows\\system32\\calc.exe'))) # returns true if file path exists

print('isfile: '+str(os.path.isfile('c:\\windows\\system32\\calc.exe'))) # returns true if it has the file part
# needs the spam.png at the end
print('isdir: '+str(os.path.isdir('c:\\windows\\system32'))) # returns true if it is directory path
# cant have spam.png at the end

print()
print('getsize: '+str(os.path.getsize('c:\\windows\\system32\\calc.exe'))) # returns size of file in bytes
print('listdir: '+str(os.listdir('C:\\Users\\Sam Mallet\\Desktop\\Python Files')))
# returns all file names and folders in the file you passed it as a list

print('listdir: '+str(os.listdir('C:\\Users\\Sam Mallet\\Desktop\\Python Files')))

os.makedirs('c:\\delicious\\walnut\\waffles') # creates folders
# already created so will cause error
