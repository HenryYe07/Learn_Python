# 需要成对进行的操作会用with
# 上锁/解锁 打开/关闭 借用/归还
# with 能得到上下文管理器的表达式 as 变量: 底下写相关的代码

# 上下文管理器协议
 # __enter__ with 里的代码执行之前使用 返回的值会赋给 as
 # __exit__ with 里的代码执行结束之后会调用（里面的代码报错了也会）

class Person:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("我是"+self.name)
    def __enter__(self):
        print("进入的逻辑")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出的逻辑")
        print(exc_type, exc_val, exc_tb)
        return 1 # 这里返回一个真值就认为异常已经处理了 就不会产生报错

p1 = Person("A")
p1.speak()

with Person("张三") as p1 , Person("李四") as p2:
    p1.speak()
    p1.OOOOO()
    p2.speak()