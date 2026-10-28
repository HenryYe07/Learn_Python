import os
import time
from multiprocessing import Process

def speak():
    try:
        for index in range(10):
            print(index,"我在说话","pid:",os.getpid(),os.getppid())
            time.sleep(1)
    # 被terminal终止的进程 finally不会执行
    finally:
        # try语法里的，无论语句是否正常执行 最终都要走一下的
        print("结束")

def study():
    for index in range(15):
        print(index,"我在学习","pid:",os.getpid(),os.getppid())
        time.sleep(1)
print(100,__name__)


if __name__ == "__main__":
    p1 = Process(target=study)
    p2 = Process(target=speak)

    p1.start()
    p2.start()
    time.sleep(2)
    print("主进程要强制终止p1了")
    p1.terminate() # 向操作系统申请终止 现在只是申请发出去了，还没终止 是异步的
    p1.join() # 等p1这个进程确实结束了
    print(p1.is_alive())
    p2.join()




