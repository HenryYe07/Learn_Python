def outer():
    num = 10
    def inner():
        nonlocal num
        # 会自动产生一个地方 存储 内层函数用到的外层函数的东西
        print(num)
        num += 1
    return inner

f = outer()
f() # 本来num要被销毁的
print(f.__closure__) # (<cell at 0x1054988b0: int object at 0x1066fb6b0>,)
# 存着一个闭包单元 里面就是 num
# 并且反复调用这个函数是共享这个值的

print(f.__closure__[0])

print(f.__closure__[0].cell_contents)
f()
f()
f() # num会持续变大

# 闭包就是 内层函数+被内层函数引用的,来自外层函数的变量
# 有嵌套 内层函数访问外层函数 外层返回了内层函数(这样这个包才能被存起来)

# 注意

# 多次调用外层函数产生的多个闭包不会互相影响

# 用到外层变量是可变类型(list,dict之类的),也不会相互影响
# 因为外层函数被反复调用产生的可变类型的对象,也是存在不同的地方的

def beauty(char,n):
    def showNsg(msg):
        print(char*n + str(msg) + char*n)
    return showNsg

s_msg = beauty("-",4)
s_msg("Hi")
