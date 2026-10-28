class Person():
    def __init__(self, name, age,gender):
        self.name = name # 默认 公有属性 在哪都能访问
        self._age = age  # 受保护的属性 当前类和子类可以访问 其实在外面也能访问到，但是十分不推荐
        self.__gender = gender # 私有属性 只能在当前类中访问

    @property # 想让别人和属性一样用这个东西 这就是一个getter
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        self._age = value

p1 = Person("A",12,1)
print(p1.__dict__) # {'name': 'A', '_age': 12, '_Person__gender': 1}
# 不难看出其实所谓的私有权限就是把名字改了
print(p1.name)
print(p1.age)