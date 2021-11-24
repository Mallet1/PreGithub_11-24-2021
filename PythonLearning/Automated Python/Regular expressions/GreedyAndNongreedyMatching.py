import re

batRegex=re.compile(r'Bat(wo)?man') #wo can appear in the text 0 or 1 times b/c ?
mo = batRegex.search('The adventures of Batman')
print('?: '+mo.group())

phoneRegex=re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') #first set of digits is optional b/c ?
mo=phoneRegex.search('My phone number is 555-1234. Call me tomorrow.')
print('?: '+mo.group())

#Use \? if you want to actually search for a string with a question mark in it

batRegex = re.compile(r'Bat(wo)*man') #The * means the segment can show up 0 or more times
mo = batRegex.search('The adventures of Batwowowowowowowowowoman')
print('*: '+mo.group())

batRegex = re.compile(r'Bat(wo)+man') #The + means the segment can show up 1 or more times
#mo = batRegex.search('The adventures of Batman') wouldn't work
mo = batRegex.search('The adventures of Batwoman')
print('+: '+mo.group())

haRegex = re.compile(r'(Ha){3}') #Uses curly braces around the number!!!!
mo = haRegex.search('He said "HaHaHa"')
print('Checking for Ha three times: '+mo.group())

phoneRegex=re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}') #first set of digits is optional b/c ?
mo=phoneRegex.search('My numbers are 415-444-9999,654-555-4589,645-7896')
print('Checking three phone numbers: '+mo.group())

haRegex = re.compile(r'(Ha){3,5}') 
mo = haRegex.search('He said "HaHaHa"')
print('Checking for Ha three to five times: '+mo.group())

digitRegex = re.compile(r'(\d){3,5}') #matches the earliest and longest possible string
mo = digitRegex.search('1234567890')
print('Greedy match: '+mo.group())

digitRegex = re.compile(r'(\d){3,5}?') #matches the earliest and smallest possible string
mo = digitRegex.search('1234567890')
print('Non-greedy match: '+mo.group())

#You can leave out the first or second number in the curly braces for no min or max
