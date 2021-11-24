import copy

name='Zophie a cat'
newName=name[0:7]+'the'+name[8:12]
print(newName)

spam=[0,1,2,3,4,5]
cheese=spam
cheese[1]='Hello!'
print(cheese)
print(spam)
print()
print('Same because cheese and spam are both referencing the same list')
print("Variables don't contain lists they just contain references to the list")
print('This applies to any mutable value')
print('Not immuatable values like strings and tuples')
print()

def eggs(cheese):
    cheese.append('Hello')

spam=[1,2,3]
eggs(spam)
print(spam)
print('Same thing but with a function')
print()

spam=['A','B','C','D']
cheese=copy.deepcopy(spam)
cheese[1]=42
print('Using deepcopy method to modify only cheese: '+str(cheese))
print('Spam: '+str(spam))
print()

print('Same string '+\
      'new line')
