def greet(name,/,gender,*,age,height):
    print(f"我叫{name},性别{gender},年龄{age},身高{height}")
# / 前面的必须按照位置顺序传参，*后面的必须用关键字传参
# 如果同时用到/和*，/必须写在前面

greet("张三","男",age=18,height=172)
greet("张三",gender="男",age=18,height=172)

def test1(*args): # 可以接收任意数量的位置参数，打包成一个元组
    print(args)

def test2(**args): # 可以接收任意数量的关键字参数，打包成一个字典
    print(args)

def test3(*args,**args2): # 可以同时使用，但是可变位置参数必须写在前面
    print(args)
    print(args2)
test3(1,2,3,a=1,b=2,c=3)

def test3(a,b,*args,c="aaa",**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

def welcome(n):
    if n>1:
        welcome(n-1)
    print(f"你好啊{n}")

welcome(5)

def jiecheng(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return n*jiecheng(n-1)
print(jiecheng(5))

def add(n1,n2):
    """
    add two numbers
    :param n1: 第一个数
    :param n2: 第二个数
    :return: 相加的结果
    """
    return n1+n2

add(1,2)

def add2(m1,m2):
    # 打三个“然后回车 pycharm会自动生成这个模版
    """
    add two numbers
    :param m1: 数字1
    :param m2: 数字2
    :return: 和
    """
    return m1+m2
add2(1,2)

def test(data1,data2,data3,data4,data5):
    print(data1,data2,data3,data4,data5)
list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
test(*list) # 把数组或者元组解包了后，再依次作为参数传入