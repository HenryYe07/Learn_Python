# 只关注这个对象能不能实现某个方法，不管具体类型
class Dog:
    def speek(self):
        print("1")

class Cat:
    def speek(self):
        print("2")

class Pig:
    def speek(self):
        print("3")

class Fish:
    def speek(self):
        print("4")

def make_sound(animal):
    animal.speek()

d1 = Dog()
c1 = Cat()
p1 = Pig()
f1 = Fish()

make_sound(d1)
make_sound(c1)
make_sound(p1)
make_sound(f1)