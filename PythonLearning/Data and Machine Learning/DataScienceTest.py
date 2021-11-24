class Person:
    def __init__(self, name):
        self.name = name

def person_init(self, name):
    self.name = name

def say_name(self):
    print(self.name)

new_class = type('Person', (), {'__init__': person_init, 'say_name': say_name})
x = new_class('Tim')
x.say_name()