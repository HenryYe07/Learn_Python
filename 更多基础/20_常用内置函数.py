# print(要打印的对象(可以多个),sep="",end="",file=sys.stdout,flush=False)
import time
print("加载中",end="",flush=True)

# for i in range(5):
#     print(".", end="", flush=True)  # PyCharm不会有缓存,在命令行中,flush默认false也就是有缓存,指定True后就没有缓存
#     time.sleep(1)
#
# for index in range(1,101):
#     print(f"\r已加载{index}%", end="", flush=True)
#     time.sleep(0.1)

# round函数是银行家舍入法 要舍的位等于5的时候,前面奇入偶舍
print(round(6.5))
print(round(7.5))

# divmod函数 返回的是 商和余数

names = ["张三","李四","王五"]
scores = [60,70,80]

result = zip(names,scores) # 如果其中一个数量少了,会按照少的那个来,后面的就丢了
print(list(result))

result_all = all(1,1,1,1) # 里面的东西全都是True返回True
result_any = any(0,0,1,0) # 里面的东西有一个是True返回True
print(result_all,result_any)