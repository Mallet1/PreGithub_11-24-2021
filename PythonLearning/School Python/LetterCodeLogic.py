#LetterCodeLogic by Sam Mallet

class LetterCodeLogic:
    """Encode/Decode Methods"""

    @staticmethod
    def Encode(msg):
        result = ''
        # reverse of decode...
        # if any lower case characters: convert to upper case (don't reject)
        # step through each character of msg (not a split operation)
        # take each character and turn it into unicode value (65,66, etc)
        # adjust unicode value to be our 1-26 number
        # space is still a special case of 0
        
        for i in msg:
            i = i.upper()
            n = str(ord(i) - 64)
            if i == ' ':
                n = '0'
            elif int(n) < 1 or int(n) > 26:
                n = '99'

            result += n + ' '

        return result

    @staticmethod
    def Decode(msg):
        # method to split msg string and decode number inside
        result = ''
        # separate string such as "1,26,3" into individual values:
        nums = msg.split(',') # split string into list nums elements
        # process each element of the list (e.g., '1', '26', '3')
        # step through each element of the list nums
        for x in nums:
            # convert individual string x into numeric value
            try:
                n = int(x.strip()) # n is now the integer value of string number x
                if n == 0:
                    c = ' '
                elif n < 1 or n > 26:
                    c = '?'
                else:
                    # translate valid #s 1 to 26 into A,B,C, etc
                    # based on the character values for A,B,C, etc (A=65, B=66)
                    c = chr(n + 64) # character from unicode value

            except ValueError:
                c = '?'

            result += c # last step inside for

        return result
