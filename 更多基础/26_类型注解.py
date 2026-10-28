num:int = 100 # 会让后面类型不对的出现警告 但是这不会导致报错,只会在编辑阶段产生警告
num =  'Hello'
num = [10,20,30]

price:float = 12.5
is_vip:bool = True

num:int
# 可以先写变量类型注解，以后再赋值
# python定义变量不能没有值 变量类型注解真的就是注解
# 只是告诉编辑器，以后如果出现num变量，类型是int

print(num)

# 要求hobby是列表，里面必须是str
hobby:list[str | int] = ['抽烟','喝酒','吃肥肉']
# 这种写法必须是python 3.10之后

# 如果是旧的版本
from typing import Union

hobby:list[Union[str,int]]
pass

hobby.append(100) # 这里也是可以约束到的

cities: set[str] = {'杭州'}
cities.add("南昌")

persons: dict[str,int] = {"ZhangSan":20,}
persons2: dict[str | int ,int] = {"ZhangSan":20,}

scores: tuple[int,int,int] = (10,20,30) # tuple 要给每一项分别确定
scores2: tuple[int,...] = (10,20,30,40) # ...意思是任意个数的

y = [10,20,30]
pass
y.append("123")  # 对于容器类型，里面的东西和推导出来不一致就会警告

def add(x:int,y:int) -> int:
    return x+y
# 如果有默认值，python会推导类型
def sub(x=0,y=1) -> int:
    return x-y
sub("Hi",1)

def show_nums_info(nums:list[int]) -> tuple[int,int,int]:
    return 1,2,3

def add2(*args:int,**kwargs: int | str) -> int : # kwargs传进来的key一定都是字符串，不需要限制
    return sum(args)

print(add2.__annotations__) # 获取函数的注解信息