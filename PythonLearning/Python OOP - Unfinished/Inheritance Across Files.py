from PythonFile import Frog

class Log(Frog):

	def __init__(self,num,isActive):
		super().__init__(1)
		self.isActive = isActive

	def get_isActive(self):
		return self.isActive

l = Log(1,True)
l.addOne()
print(l.get_isActive())