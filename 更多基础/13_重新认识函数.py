# 函数也是对象
a1 = 100
a2 = 'Hello'
a3 = [10,20,30]

def welcome():
    print("你好啊")

print(type(a1), type(a2), type(a3),type(welcome))

# 函数也可以追加属性
welcome.desc = '这是一个打招呼的函数'
welcome.ver = 1.0
print(welcome.desc)
print(welcome.ver)

# 可以把函数赋值给变量
sayHello = welcome
sayHello()
sayHello.ver = 1.1
print(welcome.ver) # 也会变

# 函数接受可变与不可变参数的区别
def welcome(data):
    print("修改前",data,id(data))
    data = 888
    print("修改后", data, id(data))
a = 666
print("函数调用前", a, id(a))
welcome(a)
print("函数调用后", a, id(a))

a = [10,20,30]
def welcome(data):
    print(data)
    data[2] = 99
    print(data)
welcome(a)
print(a) # 会发现，外面的也改了

def welcome():
    print("Hello")
    def show_msg(msg):
        print(msg)
    return show_msg

def caller(f):
    f()
caller(welcome)

welcome()(1)