#Depreciation by Sam Mallet

import locale
from Asset import Asset

def getChoice(prompt):
    goodVal = False
    while not goodVal:
        try:
            choice = input(prompt)
            if choice.lower() != 'y' and choice.lower() != 'n':
                print('Unknown operation: Y or N only.')
            else:
                goodVal = True
        except ValueError:
            print('Illegal input: Strings "Y" or "N" only')
            goodVal = False
    return choice

def getValue(prompt, vType):
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

def doDepreciation():
    asset = getValue('Asset Cost: ','f')
    salvage = getValue('Salvage Value: ','f')
    term = getValue('Life (years): ','i')
    dep = Asset(asset, salvage, term) #instantiation...
    if dep.isValid():
        print('For Straight Line the annual depreciation is: %s' % locale.currency(dep.getStrtLineDep(), grouping = True))
        sched = getChoice('Full Schedule (Y/N)? ')
        if len(sched) > 0 and sched[0].upper() == 'Y':
            print('Year    Beg.Value     Depreciation         End.Value')
            for i in range(0,dep.getTerm()):
                print('{:4}'.format(i + 1)
                    + '{:12,.2f} {:12,.2f} {:15,.2f}'.format(dep.getBbal(i), dep.getDep(i), dep.getEbal(i)))
    else:
        print('Asset error: ' + dep.getError())

def main():
    result = locale.setlocale(locale.LC_ALL, '')
    if result == 'C' or result.startswith('C/'):
        locale.setlocale(locale.LC_ALL, 'en_US')
    print('Welcome to the Depreciation Calculator')

    choice = getChoice('Do you have an Asset? (Y/N): ')
    while choice != 'n':
        if choice.lower() == 'y':
            doDepreciation()
        else:
            print('Operation unknown or not implemented')

        choice = getChoice('Do you have another Asset? (Y/N): ')
        print()
    print('Thanks for using the Calculator')

if __name__ == '__main__':
    main()
