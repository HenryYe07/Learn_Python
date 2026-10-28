from datetime import datetime
class Person:
    # 当一个函数被定义在类中，那么这个函数被称为方法

    # 初始化方法，主要作用：给当前正在创建的实例对象添加属性
    # 接收的参数 1.当前创建的实例对象self 、其他实例对象

    # 这里的是类属性，类属性是保存在类上的
    # 可以直接通过类访问，也可以通过实例访问
    # 通常用于保存 这个类公共的数据
    max_age = 120
    planet = '地球'

    def __init__(self,name,age,gender):
        # 这里的属性都是实例属性 类本身不具有这些属性
        self.name = name

        # 限制age的最大值
        if age <= Person.max_age:
            self.age = age
        else:
            self.age = Person.max_age

        self.gender = gender

    # 这里的方法主要是给实例用的，所以叫实例方法
    def speak(self):
        print(f"Hello,I am {self.name}, I am {self.age}, I am {self.gender}")

    # 用这个装饰过的称为类方法
    # 类方法收到的参数 有 当前类本身 和 自定义参数
    # 通常用来实现，与类相关的逻辑。例如操作类级别的信息

    @classmethod # 装饰器 仅装饰紧紧相连的 意思是 下面这个方法 是类方法
    def test1(cls): # cls 是类的简称
        # 在这里，cls可以访问到类的所有属性
        print("This is test1")

    @classmethod
    def change_planet(cls,new_planet):
        cls.planet = new_planet

    @classmethod
    def create(cls,info_str):
        name,birth_yar,gender = info_str.split("-")

        return cls(name,int(datetime.now().year)-int(birth_yar),gender)

    # 静态方法 也是保存在类上的
    # 只是单纯的定义在类中，不会收到self，cls这样的参数 只有自定义参数
    # 不会访问任何 类和实例相关的内容 通常用来定义 与类相关的工具方法
    @staticmethod
    def is_adult(birth_year):
        current_year = datetime.now().year

        age = current_year - birth_year

        if age <18:
            return False
        else:
            return True

    @staticmethod
    def mask_idCard(id):
        return id[:6]+'********'+id[-4:]

# 定义一个学生类(子类、派生类)，继承自Person(父类、超类、基类)
class Student(Person):
    pass # pass是用来占位的   这里如果直接空着，语法上会有问题 加个pass就没问题


# 创建Person类的实例
p1 = Person(name="Aaa",age=20,gender="M")
p2 = Person(name="Bbb",age=20,gender="W")
print(p1.name,p1.age,p1.gender)
p1.name="AAaa" # 这样也可以增加一个原本不存在的属性
print(p1.name,p1.age,p1.gender)

print(p1.__dict__) # 可以查看实例的所有属性

def speak_outer():
    print("hello")
p1.speak_outer = speak_outer

print(Person.__dict__)
p3 = Person(name="Aaa",age=20,gender="M")
p4 = Person(name="Aaa",age=20,gender="M")

print(p3.__dict__) # 实例身上并没有这些类属性
print(Person.max_age)
print(p3.max_age)

p3.max_age = 250 # 这样只会作用域示例自身的属性，并不会改变类的属性

Person.speak(p3) # 方法也可以直接在class调，但是self要自己传
# 能用 但是不推荐这样写

Person.test1()
Person.change_planet("月球")
print(Person.__dict__)
print(p3.planet)

p5 = Person.create("Iii-2020-M")
# 用实例也能调到类方法，但是非常不推荐

print(Person.is_adult(1999))
# 静态方法一般通过 类 去调用
# 用实例也可以调用，但是不推荐