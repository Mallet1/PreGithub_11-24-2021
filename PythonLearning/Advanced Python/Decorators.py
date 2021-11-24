
def func(f):
	def wrapper(*args, **kwargs): # allows for an infinite number of arguments passed in
		print('Started')
		rv = f(*args, **kwargs) # passes any arguments giver to the function
		print('Ended')
		return rv

	return wrapper

@func # same as func2 = func(func2)
def func2(x, y):
	print('i am func2')
	return y

@func # same as func3 = func(func3)
def func3():
	print('i am func3')


x = func2(5, 6)
print(x)




# example

import time

def timer(func):
	def wrapper(*args, **kwargs): # kwargs stands for keyword arguments
		start = time.time()
		rv = func(*args, **kwargs)
		total = time.time() - start
		print('Time:', total)
		return rv

	return wrapper

@timer
def test():
	for _ in range(100000000):
		pass

@timer
def test2():
	time.sleep(2)

test()
test2()
