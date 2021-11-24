first=input('num 1: ')
second=input('num 2: ')
last=input('num 3: ')
print('Sum = '+first+second+last)

# for more see Using the Debugger video under Debugging

import random

heads=0

for i in range(1, 1001):
    if random.randint(0,1)==1:
        heads=heads+1
    if i==500:
        print('Halfway done!') # right clicked and hit set breakpoint

print('Heads came up '+str(heads)+' times.')
