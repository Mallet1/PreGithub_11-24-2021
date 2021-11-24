import re

namesRegex = re.compile(r'Agent \w+')
message = 'Agent Alice gave the secret document to Agent Bob.'
print('Message: '+message)
print('The agents in message: '+str(namesRegex.findall(message)))
print(namesRegex.sub('REDACTED',message)) #Substitutes agents with redacted

namesRegex = re.compile(r'Agent (\w)\w*') #Puts the first letter in \1
newAgents=namesRegex.findall(message)
print('\nThe agents in message: '+str(newAgents))
print(namesRegex.sub(r'Agent \1****',message)) #Raw string b/c we want literal \
#Replaces agent names with Agent then their first letter followed by ****

re.compile(r'''
(\d\d\d-) |     # area code ( without parens, with dash
(\(\d\d\d\) )   # -or- area code with parens and no dash
\d\d\d          # first 3 digits
-               # second dash
\d\d\d\d        # last 4 digits
\sx\d{2,4}      # extension, like ''',re.VERBOSE | re.DOTALL | re.VERBOSE) # Use | for more arguments
# VERBOSE doesn't read newlines for more readable code
