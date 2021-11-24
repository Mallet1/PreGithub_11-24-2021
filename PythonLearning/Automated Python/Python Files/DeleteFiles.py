import os
import shutil

# os.unlink(filePath) will delete the file in filePath

# os.rmdir(filePath) will remove the folder in filePath if it's empty

# shutil.rmtree(filePath) will remove the folder in filePath even if not empty

# Delete will permanently delete not just recycle bin

# Dry run to test if it is deleting what I want

os.chdir('C:\\Users\\Sam Mallet\\Downloads')

for filename in os.listdir():
    if filename.endswith('.pdf'): # accidentally typed pdf not doc
        #os.unlink(fileaname)
        print(filename)

for filename in os.listdir():
    if filename.endswith('.pdf'): # accidentally typed doc not pdf
        os.unlink(filename)
# Deletes every pdf in the cwd which is downloads

import send2trash # downloaded from pip

# send2trash.send2trash(filepath) sends file to trash
