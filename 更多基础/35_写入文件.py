import time

with open('../a.txt', 'wt') as f: # w 写入（原来有的会清空） t 文本 x排它性 如果文件存在就会失败
    f.write("哈哈哈哈哈哈哈哈")

# a 模式
with open('../a.txt', 'at') as f:
    f.write("123")

# python的写入并不是每一次都写进硬盘，会先写到缓冲区
with open('../a.txt', 'at') as f:
    f.write("123")
    f.flush() # 立刻把缓冲区的东西写进去
    time.sleep(10000)
    f.write("123")
# + 打开用于更新 就是能读取也能写入 不能只有+
# r + 如果写入 会从头开始替换 （文件指针的行为还是r的）
with open('../a.txt', 'rt+') as f:
    f.seek(0,2)
    # 调整文件指针的位置
    # offset 偏移量

    # cookie 是字节的偏移 写数字可能错位 大多数中文字是3个对应一个
    # 一般不要去动中文的偏移 除了开头结尾

    # whence 参考点 0 从头计算 1 从当前位置 2 从文件末尾

    # 只写一个默认是whence
    f.write("123")

with open('../a.txt', 'wt+') as f:
    f.write("123")
    f.seek(0) # 把指针弄回去，就可以读取到写入到内容
    # 但是原有的东西还是会被清空的
    result = f.read()
    print(result)