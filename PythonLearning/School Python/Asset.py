#Asset

class Asset:

	def __init__(self, c=0.0, s=0.0, t=0):
		self.setCost(c)
		self.setSalvage(s)
		self.setTerm(t)
		self.error = ''
		if self.isValid():
			self.buildAsset()
	def setCost(self, value):
		self._cost = value
	def getCost(self):
		return self._cost

	def setSalvage(self, value):
		self._salvage = value
	def getSalvage(self):
		return self._salvage

	def setTerm(self, value):
		self._term = value
	def getTerm(self):
		return self._term

	def isValid(self):
		valid = True
		if self._cost <= 0:
			self._error = 'Cost must be positive.'
			valid = False
		elif self._salvage < 0:
			self._error = 'Salvage must be zero or greater'
			valid = False
		elif self._salvage > self._cost:
			self._error = 'Salvage must be less than cost'
			valid = False
		elif self._term <= 0:
			self._error = 'Term must be positive.'
			valid = False
		return valid

	def getError(self):
		return self._error

	def buildAsset(self):
		self._bbal = [0] * self._term
		self._dep = [0] * self._term
		self._ebal = [0] * self._term

		self._bbal[0] = self._cost
		depRate = 1 / self._term
		for i in range(0, self._term):
			if i > 0:
				self._bbal[i] = self._ebal[i-1]

			nextDep = self._bbal[i] * depRate * 2

			if nextDep < self.getStrtLineDep():
				self._dep[i] = self.getStrtLineDep()

			elif self._bbal[i] - nextDep >= self._salvage:
				self._dep[i] = nextDep

			if self._bbal[i] - self._dep[i] < self._salvage:
				self._dep[i] = self._bbal[i] - self._salvage

			self._ebal[i] = self._bbal[i] - self._dep[i]

	def getStrtLineDep(self):
		return (self._cost - self._salvage) / self._term

	def getBbal(self, mo):
		return self._bbal[mo]
	def getDep(self, mo):
		return self._dep[mo]
	def getEbal(self, mo):
		return self._ebal[mo]
