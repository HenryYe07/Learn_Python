# region
# # iterable
names = ["张三","李四","王五"]
# cities = ("北京","上海","杭州")
# msg = 'Hello'
# # 这些都是可迭代对象
# endregion

print(names.__iter__())
print(hasattr(names,"__iter__"))

it = iter(names) # 弄一个迭代器对象

print(it.__next__())
print(next(it))
print(it.__next__())
# print(it.__next__()) 后面没了就会报错

it2 = iter(names)
print(it2.__iter__())