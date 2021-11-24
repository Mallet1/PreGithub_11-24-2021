# Future Value

class Future:

    def __init__(self, a=0.0, r=0.0, t=0):
        # create 'private' variables for the class values
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self.error = ''
        if self.isValid():
            self.buildFV()

    # set and get methods 'encapsulate' data values
    def setAmt(self, value):
        self._amt = value

    def getAmt(self):
        return self._amt

    def setRate(self, value):
        self._rate = value

    def getRate(self):
        return self._rate

    def setTerm(self, value):
        self._term = value

    def getTerm(self):
        return self._term

    def isValid(self):
        valid = True
        if self._amt <= 0:
            self._error = 'Amount must be positive.'
            valid = False
        elif self._rate < 1 or self._rate > 25:
            self._error = 'Rate out of bounds: 1 to 25 only'
            valid = False
        elif self._term <= 0:
            self._error = 'Term must be positive.'
            valid = False
        return valid

    def getError(self):
        return self._error

    def buildFV(self):
        # create all values needed for annuity schedule.
        # first: 3 lists to store column values
        self._bbal = [0] * self._term
        self._intearn = [0] * self._term
        self._ebal = [0] * self._term

        self._bbal[0] = self._amt
        morate = self._rate / 12 / 100  # monthly rate in fractional form
        for i in range(0, self._term):
            if i > 0:
                self._bbal[i] = self._ebal[i - 1]

            self._intearn[i] = self._bbal[i] * morate
            self._ebal[i] = self._bbal[i] + self._intearn[i]

    def getFV(self):
        return self._ebal[self._term - 1]

    def getFVTotInt(self):
        # Interest = final value less total of deposits
        return self._ebal[self._term - 1] - self._bbal[0]

    def getFVBbal(self, mo):
        # month requested is assumed to be 1 to (including) term
        # additional extra credit: validate month and
        # raise exception if month is out of bounds
        # (handle exception in main program) - all methods taking mo parameter

        return self._bbal[mo]

    def getFVInt(self, mo):
        return self._intearn[mo]

    def getFVEbal(self, mo):
        return self._ebal[mo]
