# 函数的多返回值
def calculate(x,y):
    res = x + y
    res2 = x - y
    return res,res2

result = calculate(1,2)
print(result)

r1,r2 = calculate(1,2)
print(r1,r2)

# 参数的打包与解包

def show_info(*args,**kwargs):
    print(args) # 形成一个元组
    print(kwargs) # 形成一个字典
show_info('hello','world',"hahaha",like=False)

del show_info

def show_info(num1,num2,num3,name,age,gender):
    print(num1,num2,num3)
    print(name,age,gender)
nums = (10,20,30)
person = {"name":"张三","age":18,"gender":"male"}

show_info(*nums,**person)
# * 是把元组拆成一个一个位置参数 ** 是把字典拆成一个一个关键字参数
