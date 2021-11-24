
# computer programs store variables and things in the computer's RAM beacause that is the quickest way it can be retrieved later

# would usually create a memory error as my computer's RAM cannot store that much memory and generators aim to fix this
x = [i**2 for i in range(10000000000)]

for el in x:
	print(el)

# could write this instead so not every value in x is taking up the memory in my RAM
for i in range(10000000000):
	print(i**2)






class Gen:
	def __init__(self, n): # store last value in the generater and using that create the next one and repeat
		self.n = n
		self.last = 0

	def __next__(self):
		return self.next()

	def next(self):
		if self.last == self.n:
			raise StopIteration()

		rv = self.last ** 2
		self.last += 1
		return rv

g = Gen(1000000000000000000000)

while True:
	try:
		print(next(g))
	except StopIteration:
		break










gen = (x*x for x in range(100000)) # a simple way of creating a generator: a kind of iterable you can only iterate over once
for i in gen:
	print(i)







def gen(n):
	for i in range(n): # each yield statement you are basically adding to the return statement
		yield i ** 2 # as soon as we hit this it returns the value and pauses the function instead of just returning the value. Most similar to a return statement

# yield returns an iterable that is basically a list that you can only iterate through. When you iterate the last and current values are what is being stored in RAM to save space and time.
g = gen(10) # only returns an iterable

for i in g:
	print(i)

print(next(g)) # will get a stopIteration error if you call next more times than their are yields
print(next(g))
print(next(g))
print(next(g))







import sys

def gen(n):
	for i in range(n):
		yield i ** 2

x = [i ** 2 for i in range(10000)]
g = gen(10000)

print(sys.getsizeof(x))
print(sys.getsizeof(g))
