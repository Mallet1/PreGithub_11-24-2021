# ForeignCurrency written by Sam Mallet

import locale

rates = [0.0 for i in range(5)]
totcnames = 'EUR GBP JPY CAD RUB'.split()


def getRates():
    global rates, totcnames
    print('Please enter the currency rate per US $\n')
    for i in range(5):
        rates[i] = getValue(f'{totcnames[i]}: ', True)


def getChoice():
    choice = -1
    while choice < 0 or (choice > 5 and choice < 9) or choice > 9:
        try:
            choice = int(input('Currency? (1=EUR,2=GBP,3=JPY,4=CAD,5=RUB,9=NewRates,0=Quit): '))
            if choice < 0 or (choice > 5 and choice < 9) or choice > 9:
                print('Unknown operation: 1-5, 9 or 0 only')
        except ValueError:
            print('Illegal input: integers 0-5 or 9 only')
    return choice
            

def doValuation():
    global rates, totcnames
    qty = 0
    cval = 0.0
    grandtotal = 0.0
    totcunits = [0 for i in range(5)]
    totcval = [0.0 for i in range(5)]
    fullNames = 'Euros_Pounds Sterling_Yen_Canadian Dollars_Russian Rubbles'.split('_')

    choice = getChoice()
    while choice != 0:
        if choice == 9:
            getRates()
        else:
            qty = getValue(f'How many {fullNames[choice-1]} are you buying? ', False)
            cval = qty * rates[choice-1]
            print(str(qty) + f' {fullNames[choice-1]} has a value of %s \n'
                      %locale.currency(cval,grouping = True))
            totcunits[choice-1] = totcunits[choice-1] + qty
            totcval[choice-1] = totcval[choice-1] + cval
            
        choice = getChoice()
        
    print('Purchase Summary: ')
    grandtot = 0.0
    for i in range(5):
        print(totcnames[i] + ': '
              + str(totcunits[i]) + ' units for a value of : %s'
              %locale.currency(totcval[i],grouping=True))
        grandtot = grandtot + totcval[i]
    print('The total value of the proposed currency purchase was %s'
          %locale.currency(grandtot,grouping=True))
    

def getValue(prompt, double):
    a = -1
    while a <= 0:
        try:
            if double:
                a = float(input(prompt))
            else:
                a = int(input(prompt))
            if (a <= 0):
                print('Positive values only.')
        except ValueError:
            print('Illegal entry: positive numerics only.')

    return a


def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == 'C' or result .startswith('C/'):
        locale.setlocale(locale.LC_ALL, 'en_US')

    print('Welcome to the Foreign Currency Calculator.')

    getRates()
    doValuation()

    print('Thanks for using the currency calculator.')

if __name__ == '__main__':
    main()
