class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'I like to eat {food}')

    def sound(self, sound):
        print(f' My sound is {sound}')


class Lion(Animal):
    pass


class Cat(Animal):
    pass


MyLion = Lion('The lion')
print(MyLion.name)
MyLion.eat('meat')
MyLion.sound('Rrrrrrr')

MyCat = Cat('The cat')
print(MyCat.name)
MyCat.eat('milk')
MyCat.sound('Miau')
