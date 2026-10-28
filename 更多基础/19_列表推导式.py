# 用for循环+append实现
nums = [10,20,30,40]
result = []
for n in nums:
    result.append(n * 2)
print(result)

result2 = [n*2 for n in nums]
print(result2)

# 有条件的列表推导式
nums = [10,20,30,40]
result = [n*2 for n in nums if n >20]
print(result)

# 字典推导式
names = ["张三","李四","王五"]
scores = [60,70,80]
result = {names[index]:scores[index] for index in range(len(names))}
print(result)

# 集合推导式
names = ["张三","李四","王五"]
result = { n+"!" for n in names}
print(result)

# 没有元组推导式 这样写出来的是生成器 后面会讲
result = (n+"!" for n in names)
print(result)