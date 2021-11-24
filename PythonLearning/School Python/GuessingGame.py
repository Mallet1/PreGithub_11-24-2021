#! /usr/bin/env/python3
#Guessing Game - by Sam Mallet
import random as rand

# Global variables
prevCat = 0 # category value of previous guess
prevDiff = 0 # difference of previous guess from actual number

def getChoice():
    goodVal = False
    while not goodVal:
        try:
            choice = int(input('Game: 1=Hot/Cold, 2=High/Low, 0=Quit: '))
            if choice < 0 or choice > 2:
                print('Unknown selection: 0,1, or 2 only.')
            else:
                goodVal = True
        except ValueError:
            print('Illegal input: integers from 0 to 2 only please.')
            goodVal = False
    
    return choice

def getGuess():
    #method to return user guess, must be 1-100 or 0
    guess = -1
    while guess < 0 or guess > 100:
        try:
            guess = int(input('Guess? (1-100, 0=quit): '))
            if guess < 0 or guess > 100:
                print('Guess must be 1 to 100 or 0 to quit.')

        except ValueError:
            print('Illegal input: integers only from 0 to 100')
    return guess
            

def playHighLow(rnum):
    gcount = 0  # guess count for this round
    playing = True
    while playing: # same as saying playing == True
        guess = getGuess()
        if guess == 0:
            print('Sorry, you did not guess my number: '
                  +str(rnum) + ' in ' + str(gcount) + ' tries.')
            playing = False
        elif guess == rnum:
            print('You guessed my number in ' + str(gcount) + ' tries!')
            playing = False
        else:
            showHighLow(rnum,guess) # give response to user on failed guess
            playing = True
        gcount += 1

def showHighLow(rnum,guess):
    if guess > rnum:
        print('Sorry, that guess is too high.')
    elif guess < rnum:
        print('Sorry, that guess is too low.')

def playHotCold(rnum):
    gcount = 0  # guess count for this round
    playing = True
    while playing: # same as saying playing == True
        guess = getGuess()
        if guess == 0:
            print('Sorry, you did not guess my number: '
                  +str(rnum) + ' in ' + str(gcount) + ' tries.')
            playing = False
        elif guess == rnum:
            print('You guessed my number in ' + str(gcount) + ' tries!')
            playing = False
        else:
            showHotCold(rnum,guess) # give response to user on failed guess
            playing = True
        gcount += 1
    # end of playHotCold

def showHotCold(rnum,guess):
    global prevCat, prevDiff
    diff = abs(rnum - guess) # absolute value of difference
    category = 0 # categories will be: 1=cold, 2=warm, 3=very warm, 4=hot
    if diff >= 60:
        category = 1
        msg = 'cold'
    elif diff >= 30:
        category = 2
        msg = 'warm'
    elif diff >= 16:
        category = 3
        msg = 'very warm'
    else:
        category = 4
        msg = 'HOT'
    if category == prevCat:
        # same category as last guess so need modifier....
        if diff == prevDiff:
            msg += ' (same degree)'
        elif diff > prevDiff:
            msg += ' (getting colder)'
        else:
            if msg == 'HOT': # note: if in HOT then must say getting Hotter (not warmer)
                msg += ' (getting HOTTER)'
            else:
                msg += ' (getting warmer)'

    print('Your guess is: ' + msg)
    prevCat = category # previous category is now from latest guess
    prevDiff = diff # 'remember' difference form this guess

def main():
    print('Welcome to the guessing game')

    gameType = getChoice()
    while gameType != 0:
        rnum = rand.randint(1,100)
        print("I'm thinking of a number between 1 and 100...")
        if gameType == 1:
            playHotCold(rnum)
        elif gameType == 2:
            playHighLow(rnum)
        else:
            print("I don't know that game!")

        gameType = getChoice()
        print()

    print('Thanks for playing!')

if __name__ == '__main__':
    main()
