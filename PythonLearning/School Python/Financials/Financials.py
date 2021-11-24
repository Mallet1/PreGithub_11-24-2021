#Financials by Sam Mallet

import locale
from Annuity import Annuity
from Loan import Loan
from Future import Future

def getChoice():
    goodVal = False
    while not goodVal:
        try:
            choice = int(input('Select Operation: 1=Annuity, 2=Loan, 3=Future Value, 0=Quit): '))
            if choice < 0 or choice > 3:
                print('Unknown operation: 1, 2, 3 or 0 only.')
            else:
                goodVal = True
        except ValueError:
            print('Illegal input: integers 0 to 3 only')
            goodVal = False
    return choice

def getValue(prompt, vType):
    # vType is 'i if integer is wanted; 'f' if float is wanted'
    goodVal = False
    while not goodVal:
        try:
            if vType.lower() == 'i':
                amt = int(input(prompt))
            else:
                amt = float(input(prompt))
            goodVal = True
        except ValueError as ex:
            print('Illegal value: ' + str(ex))
            goodVal = False
    return amt

def doAnnuity():
    deposit = getValue('Monthly Deposit: ','f')
    rate = getValue('Annual Interest Rate (6.5%=6.5): ','f')
    term = getValue('Term (in months): ','i')
    ann = Annuity(deposit, rate, term) #instantiation...
    if ann.isValid():
        print('A monthly deposit of %s ' % locale.currency(deposit, grouping = True)
            + ' earning ' + '{:.2%}'.format(ann.getRate()/100)
            + ' annually after ' + str(ann.getTerm()) + ' months '
            + 'will have a final value of : %s' % locale.currency(ann.getFVA(), grouping = True))
        print('That includes interest earned of: %s' % locale.currency(ann.getFVATotInt(), grouping = True))
        sched = input('Full Schedule (Y/N)? ')
        if len(sched) > 0 and sched[0].upper() == 'Y':
            print('Month    Beg.Bal.     Deposit   Int.Earned         End.Bal.')
            for i in range(0,ann.getTerm()):
                print('{:4}'.format(i + 1)
                    + '{:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}'.format(ann.getFVABbal(i), ann.getAmt(), ann.getFVAInt(i), ann.getFVAEbal(i)))
    else:
        print('Annuity error: ' + ann.getError())

def doLoan():
    loanVal = getValue('Loan Amount: ', 'f')
    rate = getValue('Annual Interest Rate (6.5%=6.5): ', 'f')
    term = getValue('Term (in months): ', 'i')
    loan = Loan(loanVal, rate, term)  # instantiation...
    if loan.isValid():
        print('A loan of %s ' % locale.currency(loanVal, grouping=True)
              + ' charging ' + '{:.2%}'.format(loan.getRate() / 100)
              + ' annually with a term of ' + str(loan.getTerm()) + ' months '
              + 'will require a monthly payment of: %s' % locale.currency(loan.getMoPmt(), grouping=True))
        print('That includes interest charges of: %s' % locale.currency(loan.getInterest(), grouping=True))
        sched = input('Full Schedule (Y/N)? ')
        if len(sched) > 0 and sched[0].upper() == 'Y':
            print('Month    Beg.Bal.     Pmt   Int.Charged         End.Bal.')
            for i in range(0, loan.getTerm()):
                print('{:4}'.format(i + 1)
                      + '{:12,.2f} {:12,.2f} {:12,.2f} {:15,.2f}'.format(loan.getBegBal(i), loan.getMoPmt(),
                                                                         loan.getIntCharged(i), loan.getEndBal(i)))
    else:
        print('Loan error: ' + loan.getError())

def doFV():
    deposit = getValue('Initial Deposit: ', 'f')
    rate = getValue('Annual Interest Rate (6%=6): ', 'f')
    term = getValue('Enter the Term (in months): ', 'i')

    future = Future(deposit, rate, term)

    if future.isValid():
        print('A deposit of ' + str(locale.currency(future.getAmt(),grouping = True))
              + ' earning {:.2%}'.format(rate/100.0)
              + f' annually for {term} months will have a value of: ' + str(locale.currency(future.getFV(),grouping = True)))
        print('That includes interest earned of ' + str(locale.currency(future.getFVTotInt(),grouping = True)))

        sched = input('Full Schedule (Y/N)? ')
        if len(sched) > 0 and sched[0].upper() == 'Y':
            print('Month    Beg.Bal.   Int.Earned         End.Bal.')
            for i in range(0, future.getTerm()):
                print('{:4}'.format(i + 1)
                      + '{:12,.2f} {:12,.2f} {:15,.2f}'.format(future.getFVBbal(i),
                                                                         future.getFVInt(i), future.getFVEbal(i)))
    else:
        print('Future value error: ' + future.getError())

def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == 'C' or result.startswith('C/'):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print('Welcome to the Financials Calculator')

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            doAnnuity()
        elif choice == 2:
            doLoan()
        elif choice == 3:
            doFV()
        else:
            print('Operation unknown or not implemented')

        choice = getChoice()
        print()
    print('Thanks for using the Calculator')

if __name__ == '__main__':
    main()
