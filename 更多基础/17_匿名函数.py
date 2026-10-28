def add(x,y):
    return x+y
def sub(x,y):
    return x-y

def calculate(func,a,b):
    return func(a,b)

print(calculate(add,1,2))
print(calculate(lambda x,y:x+y,1,2))

hi = lambda :"hi" # 什么参数都不接受也要写:

judge = lambda x: "OK" if x > 0 else "BAD"

# lambda
# 只能写一行
# 不能用代码块 if for while 这些
# 只能写一个表达式
# 这个表达式会走动作为返回值