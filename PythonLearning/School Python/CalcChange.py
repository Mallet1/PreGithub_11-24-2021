total = 0

print('Welcome to the Change Calculator.')
print()

#getCoin method
def getCoin(cointype):
        c = -1
        while c < 0:
                try:
                        c = int(input('How many ' + cointype + ' do you have? '))
                        if c < 0:
                                print('Coin counts cannot be negative.   Please re-enter.')
                except ValueError:
                        print('Illegal input: must be a non-negative integer.   Please re-enter.')
                        c = -1
        return c

#priming read...
choice = input('Do you have change (y/n)?')
while choice[0].lower() == 'y':
        h = getCoin('HalfDollar')
        q = getCoin('Quarters')
        d = getCoin('Dimes')
        n = getCoin('Nickels')
        p = getCoin('Pennies')

        totcents = (h * 50) + (q * 25) + (d * 10) + (n * 5) + p
        total += totcents
        print()
        print('You have ' + str(totcents) + ' cent(s).')

        dollars = totcents // 100 # integer division
        cents = totcents % 100

        print('Which is ' + str(dollars) + ' dollar(s) and ' +
                str(cents) + ' cent(s).')

        choice = input('Do you have more change (y/n)? ')
        print()

dollars = total // 100
cents = total % 100

print('Thanks for using the change calculator!')
print('You had a total of ' + str(total) + ' cents')
print('which is ' + str(dollars) + ' dollar(s) and ' +
      str(cents) + ' cent(s).')
