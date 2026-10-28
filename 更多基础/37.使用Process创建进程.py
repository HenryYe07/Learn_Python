import os
import time
from multiprocessing import Process

def speak():
    for index in range(10):
        print(index,"我在说话","pid:",os.getpid(),os.getppid())
        time.sleep(1)

def study():
    for index in range(15):
        print(index,"我在学习","pid:",os.getpid(),os.getppid())
        time.sleep(1)
print(100,__name__)


if __name__ == "__main__":
    p1 = Process(target=study)
    p2 = Process(target=speak)  # 创建出来的都是当前这个python进程的子进程


    # 执行的时候，会把函数所在的py文件在新的进程里再读一遍，然后找到需要的函数 别的代码也会被执行到的，不过一般没关系
    # 但是不能又启动进程 会循环

    p1.start() # 调用线程实例的 start 方法 就会立刻找系统申请一个进程，并且交给操作系统调度
    p2.start() # 跟操作系统说完要开这个进程后就不等了，继续往下走
    # 如果在这里不限制必须是主程序，就会反复启动

    # 虽然主进程自己定义了这些，但是子进程还是会重新读取代码（把当前文件作为模块），重新拿到定义，然后执行



