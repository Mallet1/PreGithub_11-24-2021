import re

message='My number is 415-555-4242'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search(message) #.search returns a match object
print(mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo=phoneNumRegex.search(message)
print('.group(1): '+mo.group(1))
print('.group(2): '+mo.group(2))

message='My number is (415) 555-4242'
phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo=phoneNumRegex.search(message)
print('new .group(): '+mo.group())

batRegex=re.compile(r'Bat(man|mobile|copter|bat)') #Must contain one phrase after Bat
mo = batRegex.search('Batmobile lost a wheel')
print('\n'+mo.group())
print('.group(1): '+mo.group(1))
