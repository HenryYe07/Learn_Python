# 装饰器会接受一个函数作为参数 然后返回一个函数
# 可以在不用修改原函数的前提下,加强原函数的功能

def add(x,y):
    res = x+y
    print(f"x和y相加的结果是{res}")
    return res


def say_hello(func):
    def wrapper(*args,**kwargs):
        print("Hello")
        return func(*args,**kwargs)

    return wrapper

add_pro = say_hello(add) # 这是手动装饰 并不是很好用
add_pro(1,2)

@say_hello # 自动装饰 要求这个函数 必须接受一个函数 返回一个函数 语法糖
def add(x,y):
    res = x+y
    print(f"x和y相加的结果是{res}")
    return res

add(1,8)

# 带参数的装饰器
def say_hello(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print("Hello" + msg)
            return func(*args, **kwargs)
        return wrapper
    return outer


@say_hello("加法")
def add(x,y,z):
    res = x+y+z
    print(f"x,y和z相加的结果是{res}")
    return res

@say_hello("减法") # 用这个函数返回的东西(也是一个函数)作为装饰器装饰下面的东西
def sub(x,y):
    res = x-y
    print(f"x和y相减的结果是{res}")
    return res

sub(1,2)

# 使用多个装饰器
def test1(func):
    print("我是test1装饰器")
    def wrapper(*args,**kwargs):
        print("我是test1追加的逻辑")
        return func(*args,**kwargs)
    return wrapper

def test2(func):
    print("我是test2装饰器")
    def wrapper(*args,**kwargs):
        print("我是test2追加的逻辑")
        return func(*args,**kwargs)
    return wrapper

@test1
@test2 # 离函数近的装饰器先工作
def add(x,y):
    res = x+y
    print(f"{x}+{y}={res}")
    return res

result = add(10,2)
print(result)

# 因为 追加的都是,先执行新加的,再执行原来的,所以追加的输出顺序是先1后2


