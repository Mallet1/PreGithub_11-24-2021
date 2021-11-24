

class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self): # basically a .toString() method
		print(f'I am {self.name} and I am {self.age}')

	def speak(self):
		print("I don't know what I say")

class Cat(Pet): # basically public class Cat extends Pet
	'''def __init__(self, name, age):
		self.name = name
		self.age = age INSTEAD OF REAPEATING THESE CONSTRUCTORS'''

	def __init__(self, name, age, color):
		super().__init__(name, age)
		self.color = color

	def speak(self):
		print('Meow')

	def show(self):
		print()
		super().show()
		print(f'I am also {self.color}\n')

class Dog(Pet):
	'''def __init__(self, name, age):
		self.name = name
		self.age = age INSTEAD OF REAPEATING THESE CONSTRUCTORS'''

	def speak(self):
		print('Bark')

class Fish(Pet):
	pass

p = Pet('Tim', 19)
p.show()
c = Cat('Bill', 34, 'White')
c.show()
d = Dog('Jill', 25)
d.show()

c.speak()
d.speak()


f = Fish('Bubbles', 10)
f.speak()