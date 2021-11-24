import re

phoneRegex=re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
string='(211) 212-7366 (983) 424-4413'
print('findall(): '+str(phoneRegex.findall(string))) #Searches string for ALL matches of compile pattern
#Search only finds the number of matches you tell it to or just the first match
#returns list of strings

phoneRegex=re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') #Extra paranthesis makes them tuples
string='(211) 212-7366 (983) 424-4413'
print('findall() as tuples: '+str(phoneRegex.findall(string)))

#SHORTHAND CHARACTER CLASSES
#\d: Any numeric digit from 0 to 9
#\D Any character that is not a numeric digit from 0 to 9
#\w: Any letter, numeric digit, or the underscore character
#\W: Any character that is not a letter, numeric digit, or the underscore character
#\s: Any space, tab, or newline charcter
#\S: Any character that is not a space, tab, or newline

#Making your own character classes
vowelRegex = re.compile(r'[aeiou]') # Same as r'(a|e|i|o|u)'
print('findall() vowels: '+str(vowelRegex.findall('Robocop eats baby food.')))

vowelRegex = re.compile(r'[aeiou]{2}')
print('findall() pairs of vowels: '+str(vowelRegex.findall('Robocop eats baby food.')))

consonantsRegex = re.compile(r'[^aeiou .]') # Negative charactor class
print('findall() consonants: '+str(consonantsRegex.findall('Robocop eats baby food.')))
