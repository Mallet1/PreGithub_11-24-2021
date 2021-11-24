print(list(range(0,100,2)))

supplies=['pens','staplers','flame-throwers','binders']
for i in range(len(supplies)):
    print('Index '+str(i)+' in supplies is: '+supplies[i])

cat=['fat','orange','loud']
size,color,disposition=cat
print('Size = '+str(size))
print('color = '+str(color))
print('Disposition = '+str(disposition))

a='AAA'
b='BBB'
a,b=b,a
print('a = '+a)
print('b = '+b)
