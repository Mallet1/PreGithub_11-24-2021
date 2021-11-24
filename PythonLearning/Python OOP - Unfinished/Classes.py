

class Dog:
	def __init__(self, name, age):
		self.name = name # self.name is an attribute
		self.age = age

	def bark(self):
		print(self.name)

	def set_age(self, age):
		self.age = age

	#def add_one(self,x):
	#	return x+1


d = Dog('sam', 20)
d.set_age(d.age+1)
d.age += 1
print(d.age)

#print(d.add_one(5))