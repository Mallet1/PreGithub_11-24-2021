import random
answer=random.randint(1,20)
#print(answer)
guesses=0
guess=0
print('sup wats ur name')
name=input()

print('Well '+name+' I am thinking of a number 1 to 20.')
print('Take a guess')

for x in range(1,7):
    guesses+=1
    guess=int(input())
    if guess>answer:
       print('Too high')
    if guess<answer:
        print('Too low')
    if guess==answer:
        print('You got it!')
        break
    print('try again')

if guesses==6:
    print('You suck the number was '+answer)
else:
    print('nice')
