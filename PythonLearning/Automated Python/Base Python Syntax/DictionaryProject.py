import pprint

message='A bright happy cat flew all way to the moon and back'

count={}

for character in message.upper():
    count.setdefault(character,0)
    count[character]=count[character] + 1

print(count)

print()

pprint.pprint(count)

print()

rjtext=pprint.pformat(count)
print(rjtext)
 
