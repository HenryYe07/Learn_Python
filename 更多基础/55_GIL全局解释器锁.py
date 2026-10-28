# 线程能拿到所在进程的变量,并且也能修改,线程之间也都可以共享来自同一个进程的变量

# 某一个时刻,一个进程里 只会有一个python线程在运行

# 释放:
# 主动释放:IO操作
# 被动释放:任务超时 运算量过大 会强制给下一个
import sys
print(sys.getswitchinterval()) # 0.005s 5ms 超过五毫秒就会给下一个
# python的多线程本质上是并发(也就是快速切换) 不是并行

# 锁是解释器锁的 一般是CPython 会有 有些解释器没有这个锁

from threading import current_thread,Thread,Lock
import time

current = 0
def sale(lock_ticket):
    global current
    while True:
        with lock_ticket:
            if current <= 20:
                print(f"{current_thread().name}卖出了第{current}张票")
                current = current + 1
                time.sleep(0.03)
            else:
                print("卖完了")
                break

if __name__ == "__main__":
    lock_ticket = Lock()

    t1 = Thread(target= sale, name= "Window 1",args=(lock_ticket,))
    t2 = Thread(target= sale, name= "Window 2",args=(lock_ticket,))
    t3 = Thread(target= sale, name= "Window 3",args=(lock_ticket,))

    t1.start()
    t2.start()
    t3.start()


