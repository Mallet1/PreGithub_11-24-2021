import re
beginsWithHelloRegex=re.compile(r'^Hello') #checks if 'Hello' is at the beginning
mo = beginsWithHelloRegex.search('Hello there')
print(mo.group())

endsWithWorldRegex=re.compile(r'world!$') #checks if 'world!' is at the end
mo = endsWithWorldRegex.search('Hello world!')
print(mo.group())

allDigitsRegex=re.compile(r'^\d+$') #Must begin and end with this pattern
mo=allDigitsRegex.search('321654653654') #('31654x54653') would be false
print(mo.group())

atRegex=re.compile(r'.at') #Can have ANY character here b/c the '.'
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

atRegex=re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

print()

#Anything you find after 'FirstName: ' is stored for the .* same for last
#Doesn't count the newline character
nameRegex=re.compile(r'First Name: (.*) Last Name: (.*)') #Is greedy
print(nameRegex.findall('First Name: Al Last Name: Sweigart'))

nameRegex=re.compile(r'<(.*?)>') #Is non-greedy
print(nameRegex.findall('<To serve humans> for dinner.>'))
nameRegex=re.compile(r'<(.*)>') #Is greedy
print(nameRegex.findall('<To serve humans> for dinner.>'))

prime = 'Serve the public trust.\nProtect the innocent. \nUpload the law.'
print('\nString: \n'+prime)
dotStar = re.compile(r'.*',re.DOTALL) 
print('\ndotStar.search that counts newlines: '+str(dotStar.search(prime).group()))
#re.DOTALL to check for newlines

vowelRegex=re.compile(r'[aeiou]',re.I) #includes capital letters
print('\nre.I: '+str(vowelRegex.findall('Al, who is RoboCop?')))
