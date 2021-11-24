from queue import Queue as q
import inspect


class Person:
	def __init__(self,name):
		self.name = name

	def __repr__(self): # allows you to print an instance of Person
		return f'Person {self.name}'

	def __mul__(self, x):
		if type(x) is not int:
			raise Exception('Invalid argument, must be int')

		self.name = self.name * x

	def __call__(self, y):
		print(y)

	def __len__(self):
		return len(self.name)

p = Person('tim')
p * 4
print(p)
p(4)
print(len(p))

print()

class Queue(q):
	def __repr__(self):
		return f'Queue({self._qsize()})'

	def __add__(self, item):
		self.put(item)

	def __sub__(self, item):
		self.get()

q = Queue()
q + 2
q + 6
q - 5
print(q)
