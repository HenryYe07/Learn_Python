# 包含 __call__ 方法的类 就是一个类装饰器
# 和函数装饰器一样，接受一个函数作为参数，返回一个新的函数

class SayHello:
    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print("Hello")
            return func(*args,**kwargs)
        return wrapper



def add(x,y):
    res =  x + y
    print(f"相加的结果是{res}")
    return res
result = add(10,20)
print(result)

dec_say = SayHello()
result = dec_say(add)
print(result(10,20))

@SayHello()
def add2(x,y):
    res =  x + y
    print(f"相加的结果2是{res}")
    return res

add2(10,20)

# 带参数的类装饰器
class SayHello2:
    def __init__(self,msg):
        self.msg = msg

    def __call__(self,func):
        def wrapper(*args,**kwargs):
            print(f"Hello{self.msg}")
            return func(*args,**kwargs)
        return wrapper
@SayHello2('hahahah')
def add3(x,y):
    res =  x + y
    print(f"相加的结果2是{res}")
    return res

add3(10,20)