# map 函数
# map(操作函数,可迭代对象)

# 统一数据处理
nums = [10,20,30,40]
result = map(lambda x:x*2,nums) # map函数的返回值是一个迭代器对象 还没讲
# 需要自己去遍历 或者手动类型转换变成list之类的
res = list(result)
print(res)

for i in res:
    print(i)

str1 = ("Hello","I","am","fine")
str_map = map(lambda x:x.upper(),str1)
print(list(str_map))

# map 不是立刻把结果算出来，只有结果需要的时候才算出来

# 迭代器被迭代过了就会被耗尽
# 现在再 print(list(str_map)) 出来是空的


# filter 函数
# 选出符合条件的 组成一组新数据
# filter(过滤函数,可迭代对象)
# 返回的也是迭代器对象
nums = [10,20,30,40,50]
result_flt = filter(lambda x:x>30,nums)
print(list(result_flt))

persons = [
    {"name":"张三","age":17,"gender":"1"},
    {"name":"李四","age":18,"gender":"1"},
    {"name":"王五","age":19,"gender":"0"}
]

person_flt = filter(lambda x:x['age']>=18,persons)
# 如果不写判断函数 默认去除值为“False的值”
data = [0,1,'','hi',[],(),5]
result_2 = filter(None,data)

print(list(person_flt))
# 也是迭代器 读过一遍就没了

print(list(result_2))

# sorted(可迭代对象,key=xxx,reverse=1)

nums = [30,40,20,10]
result = sorted(nums,reverse=True)
print(result)

names = ['Python','SQL','Java']
result2 = sorted(names,key=lambda x:len(x))
result2 = sorted(names,key=len) # key需要是一个接受一个参数的函数，直接把len放这里可以
print(result2)
# 根据字典中的某个值排序
persons = [
    {"name":"张三","age":17,"gender":"1"},
    {"name":"李四","age":18,"gender":"1"},
    {"name":"王五","age":19,"gender":"0"}
]
result3 = sorted(persons,key=lambda x:x['age'])
print(result3)

# reduce(合并函数,可迭代对象,初始值)
# 要求接受两个参数

# 要从functools引入
from functools import reduce
nums = [1,2,3,4,5]

def count(a,b): # 第一个参数是前面的计算结果 第二个是新来的参数
    return a+b



result = reduce(count,nums,10)
print(result)

result = reduce(lambda a,b:a+b,nums,0)
print(result)