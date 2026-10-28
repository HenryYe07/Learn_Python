import os
import time
from multiprocessing import Process
from threading import get_native_id,Thread,RLock

def speak(lock):
    for index in range(10):
        lock.acquire()
        print(index,"我在说话","pid:",os.getpid(),"线程的编号是",get_native_id())
        lock.release()
        time.sleep(1)


def study(lock):
    for index in range(15):
        with lock:
            print(index,"我在学习","pid:",os.getpid(),'线程的编号是',get_native_id())
        time.sleep(1)
print(100,__name__)


if __name__ == "__main__":
    print("---start---","pid是",os.getpid(),"线程是",get_native_id())
    lock = RLock() # 也有RLock确保原子性
    t1 = Thread(target=study,args=(lock,))
    t2 = Thread(target=speak,args=(lock,))
    # 还是在主进程里运行的,但是开启了多个线程

    # 因为开启进程要分配的资源很多 分配网络 文件 内存 等等
    # 所以切换比较慢

    # CPU在线程之间切换是非常快的 所以---end---前面就会出现一些东西
    # 并且多个线程的任务之间 抢控制台输出的情况也会变得更加明显

    # 线程能拿到所在进程的变量, 并且也能修改, 线程之间也都可以共享来自同一个进程的变量

    t1.start()
    t2.start()

    t1.join()
    t2.join() # 也可以用join让主线程等待

    print("---end---")






