# Loan class
class Loan:
	"""Loan Calculator"""

	def __init__(self,a=0.0, r=0.0, t=0):
		# complete constructor to store
		# starting values in global 'private' variables
		# and check validity, build if ok
		self.setAmt(a)
		self.setRate(r)
		self.setTerm(t)
		self.error = ''
		if self.isValid():
			self.buildLoan()



	def buildLoan(self):
		# monthly payment calculation...
		# calculate morate...
		# calculate denominator: ((1 + monthly rate) ** term) - 1
		# calculate monthly payment: (monthlyrate + monthlyrate/denominator) * loanamt
		self._bbal = [0] * self._term
		self._intcharge = [0] * self._term
		self._ebal = [0] * self._term

		self._bbal[0] = self._amt
		morate = self._rate / 12 / 100  # monthly rate in fractional form
		for i in range(0, self._term):
			if i > 0:
				self._bbal[i] = self._ebal[i - 1]

			self._intcharge[i] = self._bbal[i] * morate
			self._ebal[i] = self._bbal[i] + self._intcharge[i] - self.getMoPmt()

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

	def getMoPmt(self):
		rate = self._rate / 100
		return (rate/12 + (rate/12) / (((1 + (rate/12)) ** self._term) - 1)) * self._amt

	def getInterest(self):
		tot = 0
		for val in self._intcharge:
			tot += val
		return tot


	def getBegBal(self, mo):
		return self._bbal[mo]
	def getIntCharged(self, mo):
		return self._intcharge[mo]
	def getEndBal(self, mo):
		return self._ebal[mo]