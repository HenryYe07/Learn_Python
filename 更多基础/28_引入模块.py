
def func1():
    pass
def func2():
    pass
def func3():
    pass

def private_func():
    pass
__all__ = ["func1", "func2", "func3"]
# 后续通过 from *** import * 引入的时候 只有在这个列表里的
# 但是 直接写具体名字还是可以引进来的

print(__name__) # 如果是直接运行这个的 值就是 __main__
# 否则就是所在的文件名

if __name__ == "__main__":
    func1()
    func2()
    func3()
    # 直接运行这个模块的时候运行。方便测试