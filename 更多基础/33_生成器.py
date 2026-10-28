# def demo():
#     print("函数开始执行了")
#     print(100)
#     yield # 函数里有这个关键字，就是生成器函数 哪怕写在一个不可能到达的地方比如
#     if 1==2:
#         yield # 函数也会因此成为生成器函数
# 生成器函数应该返回生成器对象
# d = demo()
# print(d)
# 生成器是一种特殊的迭代器

def demo():
    print("demo函数开始执行")
    print(100)
    yield 0
    a = 200
    print(a)
    yield
    b = 300
    yield 1 # 这里的表达式会在next的时候作为返回值
    print(b)
    return "AaaAaaAa"
d = demo()
print(d)
print(next(d)) # 调用了__next__方法就会开始执行。遇到yield就会暂停
print(next(d))
print(next(d)) # 遇到return 会抛出 StopIteration异常 和iteration一样的 会把return的内容作为异常信息


d = demo() # 这会是一个生成器对象
print(d.__iter__)
print(d.__next__)

# 生成器对象的__iter__ 方法返回的也是自身
print("=============")
for item in d:
    print("这是返回值"+str(item))
def create_car(total):
    for index in range(total):
        yield f"这是第{index}辆车" #yield可以写在循环里
car_gen= create_car(100)
print(next(car_gen))
print(next(car_gen))
print(next(car_gen))
# for a_car in car_gen:
#     print(a_car)

def demo():
    nums = [10,20,.30,40]
    yield from nums # 会把后面这个可遍历对象的东西 一个一个传出去
d = demo()
next(d)
r1 = next(d)
print(r1)


# def demo():
#     print("demo函数开始执行")
#     print(100)
#     a = yield 0 # 给上一个yield传值
#     print(a)
#     b = yield 1
#     print(b)
#     return "AaaAaaAa"
# d = demo()
# next(d)
# r1 = next(d)
# print(r1)
#
# r2 = d.send(666) # send能把值传进去 同时也有类似next()的效果
# # 是给前一个yield传值 虽然停在1这个位置 但是值是传给0的那个yield的
# print(r2)

# 用生成器实现遍历person
class Person:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        yield self.name
        yield self.age
        yield self.gender
        yield self.address
        # 这个函数会返回一个生成器对象

p1 = Person("张三",20,1,"浙江")


for attr in p1:
    print(attr)


# 更简单的写法
class Person:
    def __init__(self,name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.__attr = [name,age,gender,address]

    def __iter__(self):
        yield from self.__attr

p1 = Person("张三",20,1,"浙江")


for attr in p1:
    print(attr)

def fibo(total):
    pre = 1
    cur = 1
    for index in range(total):
        if index < 2:
            yield 1
        else:
            val = pre + cur
            pre = cur
            cur = val
            yield val
for i in fibo(10):
    print(i)
# 迭代器可以用 tuple list set 把里面所有东西一下子都掏出来
# 但是会一口气全算出来，可能会爆内存

# 生成器表达式
a =  (x^2 for x in range(10)) # 圆括号是生成器表达式 以前讲的方括号的是列表推导式
print(a)
# 每个结果的产生，只依赖当前这一个元素 比如翻倍 就可以用生成器表达式