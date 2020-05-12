class Animal:
    def __init__(self, name):
        self.name = name

class Lion(Animal):
    def eat(self):
        print(f'I like to eat meat')
    def sound(self):
        print(f' My sound is RRRRRRR')


class Cat(Animal):
    def eat(self):
        print(f'I like to eat milk')
    def sound(self):
        print(f' My sound is Miau')

MyLion = Lion('The lion')
MyCat = Cat('The cat')
list_animals=[MyLion, MyCat]
for i in list_animals:
    print(i.name)
    i.eat()
    i.sound()
