#Conversions by Sam Mallet

from Converter import Conversions as c

def main():
    print('Welcome to the English-Metric Converter')

    isKelvin = False
    kelvin = ''
    
    while(kelvin.lower() != 'y' and kelvin.lower() != 'n'):
        kelvin = input('On Temp conversions, would you also like to see degrees Kelvin (K) in the results? (Y/N): ')
        if kelvin.lower() == 'y':
            isKelvin = True
        elif kelvin.lower() == 'n':
            isKelvin = False
        else:
            print('Unknown input: Try again using only Y or N.')

    # remember to ask Kelvin y/n and set condition accordingly

    choice = -1
    while choice != 0:
        try:
            choice = getChoice()
            if choice == 1: # miles to kilometers                
                mi = input('Enter your miles: ')
                km = c.MitoKm(mi)
                print(f'{round(float(mi),3)} miles = {round(float(km),3)} kilometers.')
                
            elif choice == 2: # Ounces to Grams
                oz = input('Enter your ounces: ')
                gr = c.OztoGr(oz)
                print(f'{round(float(oz),3)} ounces = {round(float(gr),3)} grams.')
                
            elif choice == 3: # Fahrenheit to Celcius
                f = input('Enter your temperature in fahrenheit: ')
                ce = c.FtoC(f)
                
                if c.DegreesK(float(ce)) < 0:
                    print('This temperature is not possible, as it is below 0 K')
                    choice = getChoice()
                    continue
                
                print(f'{round(float(f),3)} degrees fahrenheit = {round(float(ce),3)} degrees celcius.')
                if isKelvin:
                    print('This is also a temperature of: ' + str(round(c.DegreesK(ce),3)
                                                                  ) + ' Kelvin')
            elif choice == 4: # Celcius to Fahrenheit
                
                ce = input('Enter your temperature in celcius: ')

                if c.DegreesK(float(ce)) < 0:
                    print('This temperature is not possible, as it is below 0 K')
                    choice = getChoice()
                    continue
                
                f = c.CtoF(ce)
                
                print(f'{round(float(ce),3)} degrees celcius = {round(float(f),3)} degrees fahrenheit.')
                if isKelvin:
                    print('This is also a temperature of: ' + str(round(c.DegreesK(float(ce)),3)) + ' Kelvin')

            elif choice == 5: # Meters to Feet
                m = input('Enter your distance in meters: ')
                ft = c.MtoFt(m)
                print(f'{round(float(m),3)} meters = {round(float(ft),3)} feet.')

            elif choice == 6: # Liters to Gallons
                li = input('Enter your liters: ')
                gal = c.LitoGal(li)
                print(f'{round(float(li),3)} liters = {round(float(gal),3)} gallons.')
                
            else:
                print('Unknown conversion')
        except ValueError as e:
            print('Data Error: ' + str(e))
        except Exception as ex:
            print('General Error: ' + str(ex))
        
        print()
    print('Thanks for using the converter.')

def getChoice():
    try:
        c = int(input('Conversion? (1=Mi-to-Km, 2=Oz-to-Gr, 3=F-to-C, 4=C-to-F, 5=M-to-Ft, 6=Li-to-Gal, 0=end): '))
    except ValueError:
        raise ValueError('Must enter an integer between 0 and 6')
    return c


if __name__ == '__main__':
    main()
