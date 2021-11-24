spam=['hi','h','hello']
print(spam.index('hello'))

spam.append('moose')
print(spam)

spam.insert(1,'Chicken')
print(spam)

spam.remove('h')
print(spam)

del spam[0]
print('Delete index 0: '+str(spam))

spam=[6,4,6,8,8,5,2,1,9]
spam.sort()
print('Sort: '+str(spam))

spam.sort(reverse=True)
print('Reverse sorted: '+str(spam))

spam=['Alice','Bob','ants','badgers','Carol','cats']
spam.sort()
print('Sorted strings: '+str(spam))

spam.sort(key=str.lower)
print('Sorted ignoring case: '+str(spam))
