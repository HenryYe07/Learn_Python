# 有一个Pool对象 但是现代都是用 ProcessPoolExecutor 更安全 更工程
from concurrent.futures import ProcessPoolExecutor

# 创建进程执行器 用submit提交 用shutdown等待任务完成
import os
import time
def work(n):
    print(f"work 正在执行任务{n}---{os.getpid()}")
    time.sleep(1)
    return f"这是任务{n}的结果"
if __name__ == '__main__':
    print("---开始---")

    # 创建一个进程执行器
    Executor =  ProcessPoolExecutor(max_workers=5) # 最多三个进程干活
    # future1 = Executor.submit(work,1) # 这里参数直接往下写就行 不需要args了
    # future2 = Executor.submit(work, 2) # submit 是不阻塞的 全都先提交过去 然后轮着运行
    # future3 = Executor.submit(work, 3)
    # future4 = Executor.submit(work, 4)
    # future5 = Executor.submit(work, 5)
    # future6 = Executor.submit(work, 6)
    # future7 = Executor.submit(work, 7)
    futures = [Executor.submit(work, n) for n in range(15)]

    # print(future1)
    # print(future4.result()) # 这个方法是阻塞的


    for f in futures:
        print(f.result())
    print("---结束---")


    Executor.shutdown(wait=True)
    # 作用: 不在接受新的任务
    # wait 默认False 不阻塞主进程 改成True就会阻塞住 等进程池里所有东西执行完毕然后释放


