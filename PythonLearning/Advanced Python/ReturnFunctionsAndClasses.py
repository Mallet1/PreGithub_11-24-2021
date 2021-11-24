import inspect
from queue import Queue

def make_class(x):
	class Dog:
		def __init__(self, name):
			self.name = name

			def make_class2(x):
				class cat:
					def __init__(self):
						self.name = 'sam' # can make classes infinitely like this


		def print_value(self):
			print(x)

	return Dog # reference to class not object. Dog() would be a reference to the object

cls = make_class(10)
d = cls('Tim')
print(d.name)
d.print_value()

print()

def func(x):
	if x == 1:
		def rv(name):
			print('X is equal to 1 and your name is ' + name)

	else:
		def rv(name):
			print('X is not 1')

	return rv # can return a function to be defined in a variable

new_func = func(1)
print(type(new_func))
print(inspect.getsource(new_func)) # gets the source code behind a module, class, method, function, traceback, frame, or code object
new_func('hi')
