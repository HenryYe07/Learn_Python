from abc import ABC,abstractmethod
# 抽象类 也就是不能直接实例化的类
# 通常作为规范 让子类去继承

class MustRun(ABC): # 继承了ABC才是抽象类
    @abstractmethod # 出现这个 就不能直接创建实例了
    def run(self):
        pass

    # 也可以写常规方法，也可以正常被继承下来

class Person(MustRun):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def run(self):
        print(f"{self.name}跑步了")


