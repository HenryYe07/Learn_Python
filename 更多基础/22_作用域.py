# 全局作用域 在这个py文件内有效
# 再往外还有一个内建作用域 是Python预先定义好的东西
a = 100

def test():
    global a # 确定函数里改的是全局的

    print(a)
    a = 999 # a如果在函数中被赋值过了,那前面如果不写 global 也拿不到全局作用域的a
    print(a)
    c = 250
    d = 199

    def inner():
        nonlocal c # 不是本地的 从外层找
        print(c) # 此时,c属于外层函数作用域 自己这没有,可以向外扩拿到里面的值
        c = 299 # 修改c的值 此时修改的是外层的
    inner()
    print(d)
    print(c)

print(a)
test()
print(a)