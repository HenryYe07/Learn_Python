class Person():
    def __init__(self, name, age,gender):
        self.name = name # 默认 公有属性 在哪都能访问
        self._age = age  # 受保护的属性 当前类和子类可以访问 其实在外面也能访问到，但是十分不推荐
        self.__gender = gender # 私有属性 只能在当前类中访问

print(issubclass(Person, object))
# int str list bool 都是python内置的类 都继承了object类
print(issubclass(int, object))

for i in object.__dict__:
    print(i)
p = Person("Aaa",20,1)
print(p.__dict__) # 打印这个对象自己的东西
print(dir(p)) # 打印这个对象能够访问到的所有东西