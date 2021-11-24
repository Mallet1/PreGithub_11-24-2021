
class Person:
	number_of_people = 0 # class attribute while self is a regular attribute - mainly used for constants like gravity
	# doesn't have access to an instance (defined for entire class)

	def __init__(self, name):
		self.name = name
		Person.add_person()

	@classmethod # decorated to denote that this specific method is a class method
	def number_of_people_(cls): # wrote cls becuase it is not acting on and object (like when self is used) it is acting on the whole class
		return cls.number_of_people # not specific to an instance

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1

p1 = Person('time')
p2 = Person('Jill')

print(Person.number_of_people) # can access the class attribute with just the class
Person.number_of_people = 8
print(p2.number_of_people)
Person.number_of_people = 0

print(Person.number_of_people_())
print()




# --------------------------------------Static Methods-----------------------------------------



print()
class Math:


	@staticmethod # don't have access to an instance just like the class method, they perform a function without changing anything
	def add5(x): # no self or cls because it's not accessing anything
		return x + 5

	@staticmethod
	def pr():
		print('run')

print(Math.add5(5))
Math.pr()
