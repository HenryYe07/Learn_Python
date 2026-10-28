names = ["张三","李四","王五"]
# 迭代器是一次性的 回不去
# 但是一个可迭代对象可以创建多个迭代器
it1 = iter(names)
it2 = iter(names)

print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))

class Person:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        return PersonIterator(self)

class PersonIterator:
    def __init__(self,person):
        self.p = person # 把外部传进来的放在自己这
        self.index = 0 # 设置迭代器初始化状态 指针的位置
        self.attrs = [person.name, person.age, person.gender, person.address] # 配置好要遍历的内容
    def __iter__(self):
        return PersonIterator() # 迭代器的iter方法返回的是自身
    def __next__(self):
        if self.index >= len(self.attrs):
            raise StopIteration
        value = self.attrs[self.index]
        self.index += 1
        return value

        pass


p1 = Person("张三",18,"男","浙江杭州")

for item in p1:
    print(item)

# 实现方式2
class Person2:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

        self.__index = 0
        self.__attrs = [self.name,self.age,self.gender,self.address]
    def __iter__(self):
        return self
    def __next__(self):
        if self.__index < len(self.__attrs):
            value = self.__attrs[self.__index]
            self.__index += 1
            return value
        else:
            raise StopIteration


# 相较于list，迭代器是懒处理的，用到了才算出来，内存占用明显小