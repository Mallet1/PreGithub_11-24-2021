myCat = {'size': 'fat','color':'gray','disposition':'loud'}
print('My cat has '+myCat['color']+' fur.')

spam={12345: 'Luggage combination', 42: 'TheAnswer'}
print(spam[12345])

print()

eggs={'name': 'Zophie', 'species': 'cat', 'age':8}
ham={'species': 'cat', 'name': 'Zophie', 'age': 8}
print('eggs: '+str(eggs))
print('ham: '+str(ham))
print('eggs = ham: '+str(eggs==ham)) #Dictionaries ignore order

print()

print('"name" is in eggs: '+str('name' in eggs))

print()

print('Keys: '+str(eggs.keys()))
print('Values: '+str(eggs.values()))
print('items: '+str(eggs.items()))
#Concatenate to list to get rid of dict_

print()
      
for k, v in eggs.items():
    print(k,v) #tuples are like lists just immutable and use parenthesis


print()

print('Cat is a value: '+str('cat' in eggs.values()))

print('eggs.get("age",0): '+str(eggs.get('age', 0)))

print()

picnicItems={'apples': 5, 'cups': 2}
print('I am bringing '+str(picnicItems.get('napkins', 0))+' to the picnic.')

eggs.setdefault('color','black')
print('New eggs: '+str(eggs))

