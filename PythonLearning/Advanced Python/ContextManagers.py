
# uses example
file = open('file.txt', 'w')
file.write('hello') # if there is any error on this line the file will never close and that is a problem
file.close()

file = open('file.txt', 'w') # one way to fix the problem
try:
	file.write('hello')
finally:
	file.close()

# context manager fix (context managers often use the with keyword)
with open('file.txt', 'r') as file:
	file.write('hello') # no matter if this code works the file will still close










# writing a context manager
class File:
	def __init__(self, filename, method):
		self.file = open(filename, method)

	def __enter__(self): # with something as f ('something' would call the enter method and store the block of code in f)
		print('Enter')
		return self.file

	def __exit__(self, type, value, traceback): # code runs in the case of an exception
		print(type)
		print(value)
		print(traceback)
		print()

		self.file.close()

		return True # tells python the exeption was handled and the program can continue

with File('file.txt', 'w') as f:
	print('Middle')
	f.write('hello').sasdgzcvasd # exception calls __exit__







# using a generator to create a quick easy context manager

from contextlib import contextmanager

@contextmanager
def file(filename, method):
	print('enter')
	file = open(filename, method)
	yield file
	file.close()
	print('exit')


with file('file.txt', 'w') as f:
	print('middle')
	f.write('hello')
