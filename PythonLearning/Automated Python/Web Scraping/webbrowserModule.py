import webbrowser, requests

# webbrowser basics in PythonScripts mapit.py

# webbrowser.open('https://automatetheboringstuff.com')

# requests.get('url') returns response object of download request
res=requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.status_code) # to check if the download was successful
# 200 - everything went ok   404 - file not found

#print(len(res.text)) # the string in the text file

print(res.raise_for_status) # raises an exception if the URL doesn't exist

playFile = open('RomeoAndJuliet.txt', 'wb') # needs to be 'wb' to specify bytes
for chunk in res.iter_content(100000): # returns chunk of the content through each loop iteration
    # specify how many bytes each chunk will contain in parenthesis
    
    print(playFile.write(chunk)) # writes the chunks to RomeoAndJuliet.txt

# first iteration: returns number of bytes written to playFile
# second iteration: returns number remaining bytes
playFile.close()

