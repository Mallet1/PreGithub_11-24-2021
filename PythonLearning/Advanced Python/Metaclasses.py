
class Foo:
	def show(self):
		print('hi')

def add_attribute(self):
	self.z = 9

Test = type('Test', (Foo,), {'x':5, 'add_attribute':add_attribute}) # just a class ('class name', (often inheritence), {'attribute name':attribute value})
# or just (name, bases, attributes)

t = Test()
t.wy = 'hello'
print(t.x, t.wy)
t.show()

t.add_attribute()
print(t.z)

print()

class Meta(type): # meta class, will mostly inherit from class type
	def __new__(self, class_name, bases, attrs): # (name, bases, attributes)

		a = {}
		for name, val in attrs.items(): # changes attribute names that don't start with __ to uppercase
			if name.startswith('__'):
				a[name] = val
			else:
				a[name.upper()] = val
		print(a)
		return type(class_name, bases, a) # returns a type object that creates a class

class Dog(metaclass=Meta): # the default meta class for dog would be type but we've overridden that with metaclass=Meta
	x = 5
	y = 8

	def hello(self):
		print('hi')

d = Dog()
print(d.X)
