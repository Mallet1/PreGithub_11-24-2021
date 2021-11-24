#Letter Code by Sam Mallet
from LetterCodeLogic import LetterCodeLogic as lcl

def main():
    print('Welcome to the LetterCode program.')

    choice = getChoice()
    while choice != 0:
        if choice == 1: # Encode
            # call Encode method of LetterCodeLogic class
            msg = input('Enter a sentence to encode: ')
            result = lcl.Encode(msg)
            print(result)
        elif choice == 2:
            msg = input('Enter your numbers to decode (separated by commas): ')
            result = lcl.Decode(msg)
            
            print('Your decoded message is: \n' + result)
        else:
            print("I don't understand your request")

        print()
        choice = getChoice()
    print('Thanks for using the Letter Code program.')

def getChoice():
    # menu
    # must be robust in final version: loop and try/except
    c = -1
    
    while c < 0 or c > 2:
        try:
            c = int(input('Choice? (1=Encode, 2=Decode, 0=Quit): '))
            if c < 0 or c > 2:
                print('Error: Choice must be between 0 and 2, try again: ')
        except ValueError:
            print('Error: Must be an integer, try again: ')

        
    return c

if __name__ == '__main__':
    main()
