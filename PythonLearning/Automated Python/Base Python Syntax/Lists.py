a=['hi','hello','nword','what']
spam=[['cat','bat'],[10,20,30,40,50]]

print('a2 = '+str(a[2]))
print('spam0 = '+str(spam[0]))
print('spam[1][4] = '+str(spam[1][4]))
print('spam-1 = '+str(spam[-1]))
print('spam-2 = '+str(spam[-2]))
print('a[1:3] = '+str(a[1:3]))
a[1:3]=['h','a','d','t']
del spam[1]
print('Length of a = '+str(len(a)))
print(list('hello'))
print('"hi" in the list a? '+str(('hi' in a)))
print('"banana" not in the list a? '+str(('banana' not in a)))
