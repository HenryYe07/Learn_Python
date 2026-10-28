# 没有顺序 不能通过下标访问，自动去除重复
a = {1,True,2,3,4,5,6,6}
# True 在Py中 和1 是一样的
a.add(99)
b  = frozenset([1,2,3,4,5,6,6]) # 不可变集合
# 这里面也可以放元组之类的 可迭代对象
print(a)
print(b)
# x = {} 出来的是空字典 定义空集合应该写
c = set()
# 只有不可变的东西可以嵌套到集合里面去，比如 frozenset 和 tuple
s1 = {10,20,30}
s2 = frozenset({20,30,40})
l1 = [11,22,33]
t1 = (66,77,88)

# s3 = {11,22,33,s1} 是不行的，因为 list 类型是可变的
s3 = {11,s2,t1} # frozenset 和 tuple 是不可变的 可以塞进去

# 增
s1.add(666)
s1.update([1,2,3]) # 接收可迭代对象
s1.update(range(10))
print(s1)

# 删
s1.remove(666) # 如果这个元素不存在会报错
s1.discard(666)  # 不存在也不会报错
print(s1.pop()) # 移除任意一个元素 并且返回那个元素
s1.clear() # 清空集合，没有返回值

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}
print(s1.difference(s2)) # 找出两个集合中不一样的东西，并且返回不一样的元素组成的集合

s1.difference_update(s2) # 删除s1中 s2也有的元素

print(s1.union(s2)) # 合并两个集合 返回新的，原来的都不会变

s1 = {1,2,3}
s2 = {1,2,3,4,5}
print(s1.issubset(s2)) # 判断s1是不是s2的子集 相反也有issuperset

print(s1.isdisjoint(s2)) # 判断是不是没有交集合 如果没有返回True


# 集合相关的一些运算符

s1 = {10,20,30,40,50,60}
s2 = {40,50,60,70,80,90}

result = s1 | s2 # 并集
result = s1 & s2 # 交集
result = s1 - s2 # 差集 （属于s1 但是不属于s2的内容的集合 ）
result = s1 ^ s2 # 只属于其中一个集合的元素

# 集合不能用while循环 因为不允许用下标
# 可以用for循环
