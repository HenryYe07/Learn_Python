# 有一个Pool对象 但是现代都是用 ProcessPoolExecutor 更安全 更工程
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import get_native_id,RLock

# 创建线程执行器 用submit提交 用shutdown等待任务完成
import os
import time

def work(n,lock):
    with lock:
        print(f"work 正在执行任务{n}---{get_native_id()}")
    time.sleep(0.5)
    return n



if __name__ == '__main__':
    print("---开始---")
    # 创建一个线程锁
    lock = RLock()
    # 创建一个线程执行器
    executor =  ThreadPoolExecutor(max_workers=4) # 最多三个线程干活
    futures = [executor.submit(work,index,lock) for index in range(10)]

    executor.shutdown(wait=True)
    print("---结束---")

    for i in as_completed(futures): # 安装完成顺序
        print(i.result())


    # 作用: 不在接受新的任务
    # wait 默认False 不阻塞主线程 改成True就会阻塞住 等线程池里所有东西执行完毕然后释放


