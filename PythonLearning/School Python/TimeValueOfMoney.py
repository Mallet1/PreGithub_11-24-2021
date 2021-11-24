#Time Value of Money - by Sam Mallet
import locale

def getChoice():
    #use boolean for loop control...
    goodVal = False
    while not goodVal:
        try:
            c = int(input('Select operation: 1=PV, 2=FV, 3=FV-Annuity, 0=Quit: '))
            if c < 0 or c > 3:
                #out of bounds....
                print('Unknown operation: 1-3 or 0 to quit.')
                goodVal = False
            else:
                #correct 0-3 choice
                goodVal = True
        except ValueError:
            print('Illegal input: integers from 0 to 3 only please.')
            goodVal = False
    return c

def getValue(prompt, t):
    #must be 'robust' on completion with loop and try/except
    #return must be positive float (zero or negatives rejected)
    v = 0
    while type(v) != t or v <= 0:
        try:
            v = t(input(prompt))
            if v <= 0:
                print('Number cannot be negative or zero')
        except ValueError:
            if t == int:
                print('Illegal input: must be a positive integer')
            else:
                print('Illegal input: must be a positive float')
            
    return v

def doPV():
    recieve = getValue('Amount to be received: ', float)
    interest = getValue('Annual Interest Rate (6%=6): ', float)
    term = getValue('Enter the Term (in months): ', int)

    monthly_interest = interest / 12.0 / 100.0

    present_value = recieve / ( (1 + monthly_interest)**term)

    print('An amount of %s' % str(locale.currency(recieve,grouping = True))
          + f' to be received in {str(term)} months with an annual cost of money of '
          + '{:.2%}'.format(interest/100.0) + '\n'
          + 'has a value today of: ' + str(locale.currency(present_value,grouping = True)))
    print('That includes a discount of ' + str(locale.currency(recieve-present_value,grouping = True)))

def doFV():
    initial = getValue('Initial Deposit: ', float)
    interest = getValue('Annual Interest Rate (6%=6): ', float)
    term = getValue('Enter the Term (in months): ', int)

    monthly_interest = interest / 12.0 / 100.0
    future_value = initial * (1 + monthly_interest) ** term

    print('A deposit of ' + str(locale.currency(initial,grouping = True))
          + ' earning {:.2%}'.format(interest/100.0)
          + f' annually for {term} months will have a value of: ' + str(locale.currency(future_value,grouping = True)))
    print('That includes interest earned of ' + str(locale.currency(future_value-initial,grouping = True)))

def doFVA():
    deposit = getValue('Monthly Deposit: ', float)
    #rates must be > 0 but <= 25%
    rate = getValue('Annual Interest Rate (6.5% = 6.5): ', float)
    while rate > 25.0:
        print('Rate is out of bounds. 25% is max value.')
        rate = getValue('Annual Interest Rate (6.5% = 6.5): ', float)
    term = getValue('Enter Term (in months): ', int)
    fva = 0.0 # sum of deposits plus interest earned by those deposits
    #formula requires monthly interest rate in fractional (%) form
    #(but ours was entered as an annual rate and as whole #)
    morate = rate / 12.0 / 100.0
    for i in range(term):
        intearn = (fva + deposit) * morate
        fva = fva + deposit + intearn

    print('A monthly deposit of %s ' % locale.currency(deposit,grouping = True)
          + ' earning '
          + '{:.3%}'.format(rate/100.0) + ' annually after '
          + str(term) + ' months will have a final value of: '
          + locale.currency(fva,grouping=True) )
    print(f'That includes interest earned of {locale.currency( (fva - (deposit*term)),grouping = True)}')
    
            
def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == 'C' or result.startswith('C/'):
        locale.setlocale(locale.LC_ALL, 'en_US')
    
    print('Welcome to the Financial Calculator\n')

    choice = getChoice()
    print()
    while choice != 0:
        #get data and perform calculations...
        if choice == 1:
            #PV logic
            doPV()
            print()
        elif choice == 2:
            #FV logic
            doFV()
            print()
        elif choice == 3:
            #FV - Annuity logic
            doFVA()
            print()
        else:
            print('Unknown operation.')
            

        #ask user for next operation or quit
        choice = getChoice()
        print()

    print('Thanks for using the Finanacial Calculator!')

# launch program based on encironment variable __name__
if __name__ == "__main__":
    main()
