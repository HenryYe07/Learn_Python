import os
import time
from multiprocessing import Process,Lock,RLock,current_process

def speak(loc):
    for index in range(10):
        # 上锁 : 如果锁此时空闲 立刻上锁
        # 如果锁在别人那锁着，那会等别人把锁解开
        loc.acquire() # Lock的锁给同一个锁连上两次也会卡死
        # RLock的锁可以重复上 一个进程可以重复获取已经持有的锁 全都解开了才会允许另一个进程上这个锁
        print("AAAAAAAAAAAA")
        print("BBBBBBBBBBBB")
        print("CCCCCCCCCCCC")
        print("DDDDDDDDDDDD")
        print("EEEEEEEEEEEE")
        # 这里如果有错的代码，会卡死 但是不会退出 锁不会被释放
        loc.release() # acquire 和release必须成对出现 不然会卡死
        time.sleep(0.1)
        

def study(lock):
    for index in range(15):
        with lock: # 也可以用with
            print("1")
            print("2")
            print("3")
            print("4")
            print("5")
            # 这里有错误 锁还是会被释放
        time.sleep(0.1)

print(100,__name__)


if __name__ == "__main__":
    lock = Lock()

    p1 = Process(target=study,args=(lock,)) # 还有kwargs
    p1.start()
    # p1.join(5) # 让主进程等p1执行完再去执行后面的代码
    # 这里面写一个数字 就是等待指定的秒数

    p2 = Process(target=speak,args=(lock,))
    p2.start()
    # p2.join() 这种写法又变回同步了，多进程没有意义

    p1.join()
    p2.join()
    print("All Done")
    # current_process().join() 只能把子进程join

    # 是让执行p1的那个进程等 阻塞一段时间 或者阻塞到指定时间
    # 必须start后再join

# 进程之间不共享内存 也不会共享任何变量
# 开了Global也不行 进程之间是相互隔离的








