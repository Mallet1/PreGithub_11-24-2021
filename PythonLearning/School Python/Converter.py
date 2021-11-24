# Converter methods by Sam Mallet

class Conversions:
    '''Conversion Algorithms'''

    @staticmethod
    def MitoKm(mi):
        if not isinstance(mi,(int,float)):
            # bubble up exception for non-numerics as General Exception
            try:
                mi = float(mi)
            except ValueError:
                raise Exception('Miles input was not numeric')
        if mi <= 0:
            # error: not a legal value for conversion
            # bubble up ValueError
            raise ValueError('Miles must be positive')
        
        km = mi * 1.60934
        return km

    @staticmethod
    def OztoGr(oz):
        if not isinstance(oz,(int,float)):
            # bubble up exception for non-numerics as General Exception
            try:
                oz = float(oz)
            except ValueError:
                raise Exception('Ounces input was not numeric')
        if oz <= 0:
            # error: not a legal value for conversion
            # bubble up ValueError
            raise ValueError('Ounces must be positive')
        
        gr = oz * 28.3495
        return gr

    @staticmethod
    def FtoC(f):
        if not isinstance(f,(int,float)):
            # bubble up exception for non-numerics as General Exception
            try:
                f = float(f)
            except ValueError:
                raise Exception('Fahrenheit input was not numeric')
        
        c = (5 / 9) * (f - 32)
        return c

    def CtoF(c):
        if not isinstance(c,(int,float)):
            # bubble up exception for non-numerics as General Exception
            try:
                c = float(c)
            except ValueError:
                raise Exception('Celcius input was not numeric')
        
        f = 9 / 5 * c + 32
        return f

    @staticmethod
    def DegreesK(temp):
        return temp + 237.15

    @staticmethod
    def MtoFt(m):
        if not isinstance(m,(int,float)):
            # bubble up exception for non-numerics as General Exception
            try:
                m = float(m)
            except ValueError:
                raise Exception('Meters input was not numeric')
        if m <= 0:
            # error: not a legal value for conversion
            # bubble up ValueError
            raise ValueError('Meters must be positive')
        
        ft = m * 3.2808
        return ft

    @staticmethod
    def LitoGal(li):
        if not isinstance(li,(int,float)):
            # bubble up exception for non-numerics as General Exception
            try:
                li = float(li)
            except ValueError:
                raise Exception('Liters input was not numeric')
        if li <= 0:
            # error: not a legal value for conversion
            # bubble up ValueError
            raise ValueError('Liters must be positive')
        
        gal = li * .26417
        return gal
            

    
