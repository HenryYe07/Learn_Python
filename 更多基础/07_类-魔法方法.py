# 魔法方法： __xxx__命名的方法
class Person():
    def __init__(self, name, age,gender):
        self.name = name # 默认 公有属性 在哪都能访问
        self._age = age  # 受保护的属性 当前类和子类可以访问 其实在外面也能访问到，但是十分不推荐
        self.__gender = gender # 私有属性 只能在当前类中访问

    def __str__(self): # print 或者 转换成str的时候都会调用这个
        return f"{self.name}-{self._age}-{self.__gender}"
    def __len__(self):
        pass
    def __lt__(self, other): # lt: less than  gt: greater than eq: equal
        pass
    def __getattr__(self, name):
        return f"{name} 不存在"
p1 = Person("Aaa",20,1)
print(p1.p)
