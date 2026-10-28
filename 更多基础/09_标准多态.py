class Animal:
    def speek(self):
        print("动物正在发出声音")

class Dog(Animal):
    def speek(self):
        print("Wang")

class Cat(Animal):
    def speek(self):
        print("Miao")

def make_sound(animal:Animal): # 类型注解 要求传入的实例 必须是Animal类或者其子类的实例对象
    animal.speek()

a1 = Animal()
d1 = Dog()
c1 = Cat()

class Pig:
    def speak(self):
        print("yue")
p1 = Pig()
make_sound(p1) # Python里这样写能用，但是不推荐