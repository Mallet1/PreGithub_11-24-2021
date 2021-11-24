def isPhoneNumber(text):
    if len(text)!=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNumber('314-589-6214'))
message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

foundNumber=False
for i in range(len(message)):
    chunk=message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+chunk)
        foundNumber=True
if not foundNumber:
    print('Could not find any phone numbers.')

#Regular expression way
print('\n'+'Regular expressions'.center(80,'-')+'\n')

import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #Creates regular expression object
mo = phoneNumRegex.search(message) 
print('.search: '+str(mo.group()))
print('.findall: '+str(phoneNumRegex.findall(message)))
