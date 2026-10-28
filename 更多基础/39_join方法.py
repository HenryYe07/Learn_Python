import os
import time
from multiprocessing import Process,Lock,RLock

def speak(loc):
    for index in range(10):
        loc.acquire()
        print("AAAAAAAAAAAA")
        print("BBBBBBBBBBBB")
        print("CCCCCCCCCCCC")
        print("DDDDDDDDDDDD")
        print("EEEEEEEEEEEE")
        loc.release() 
        time.sleep(0.1)
        

def study(lock):
    for index in range(15):
        with lock: 
            print("1")
            print("2")
            print("3")
            print("4")
            print("5")
        time.sleep(0.1)

print(100,__name__)


if __name__ == "__main__":
    lock = Lock()

    p1 = Process(target=study,args=(lock,)) 
    p2 = Process(target=speak,args=(lock,))

    p1.start()
    # p1.join() 写成这样没有意义 相当于还是同步到代码。
    # p1.join(5) # 最多等待5秒然后往下

    p2.start()
    # p2.join()

    p1.join()
    p2.join() # 等两个都完成了才Done 但是两个东西本身都是持续管自己的
    # join方法其实是等待这个进程退出
    # 可能是因为执行完了，也可能是被强制退出了
    print("All Done")




