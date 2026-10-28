# 按照完成的顺序获取结果
from concurrent.futures import ProcessPoolExecutor, as_completed

# 创建进程执行器 用submit提交 用shutdown等待任务完成
import os
import time
def work(n):
    if n == 1:
        time.sleep(10)
    elif n == 2:
        time.sleep(5)
    else:
        time.sleep(1)

    print(f"work 正在执行任务{n}---{os.getpid()}")
    return f"这是任务{n}的结果"

if __name__ == '__main__':
    print("---开始---")

    # 创建一个进程执行器
    Executor =  ProcessPoolExecutor(max_workers=5) # 最多三个进程干活
    futures = [Executor.submit(work, n) for n in range(15)]

    print(as_completed(futures))
    for f in as_completed(futures):
        print(f.result()) # 这样是按照提交的顺序输出结果的
    print("---结束---")


    Executor.shutdown(wait=True)


