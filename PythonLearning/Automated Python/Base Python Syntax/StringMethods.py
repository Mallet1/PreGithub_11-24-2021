spam='Hello world!'
print('Spam uppercase: '+spam.upper())
print('Spam lowercase: '+spam.lower())
spam=spam.upper()
print('Spam is upper: '+str(spam.isupper()))
print('Spam is lower: '+str(spam.islower()))

#isalpha() - letters only
#isalnum() - letters and numbers only
#isdecimal() - numbers only
#isspace() - whitespace only
#istitle() - titlecase only
#(begins with upper case letter followed by only lowercase)
#startswith() - true if a string begins with a string it is compared to
#endswith() - true if a string ends with a string it is compared to
#join() - returns a combined string of every string value in a list
#find() - returns the index of a string in a string

print('.join(): '+', '.join(['cats','rats','bats']))
#The string before the list displays what will be between each string

#split() - splits a string where ever you want it to and returns a list

print('My name is Simon'.split(' '))

#ljust() rjust() = returns a padded version of a string
#with spaces to right or left justify the text

print('Hello right justified'.rjust(60))
print('Hello left justified with asterisks'.ljust(60,'*'))

#.center() - centers the text with a certain length

print('Hello centered'.center(60,'='))

#strip() - strips white spaces from both sides of the string
#rstrip() - strips white spaces from the right side of the string
#lstrip() - strips white spaces from left side of the string
#These can also remove certain letters from either side
#replace() - Replaces a string segment with another string segment

#pyperclip.copy and pyperclip.paste - copies and pastes things to clipboard

name='Alice'
place='Main Street'
time='6 pm'
food='turnips'
print('Hello %s, you are invited to a party at %s at %s. please bring %s.'
      % (name,place,time,food))
