# map方法 批量提交 得到结果的顺序和任务分配顺序一致

from concurrent.futures import ProcessPoolExecutor, as_completed

import os
import time
def work(n):
    if n == 1:
        time.sleep(10)
    elif n == 2:
        time.sleep(5)
    else:
        time.sleep(1)

    return f"这是任务{n}的结果"

if __name__ == '__main__':
    print("---开始---")

    executor =  ProcessPoolExecutor(max_workers=3) # 最多三个进程干活

    results = executor.map(work,[1,2,3,4,5,6,7])
    # 如果要传锁进去
    # results = executor.map(work,[1,2,3,4,5,6,7],[lock]*7)
    # 拿第一个可迭代对象作为第一个参数 第二个作为第二个参数...


    # 后面这个迭代器对象里的东西,会作为参数传进去
    # 返回的是生成器
    # 立刻就会拿到生成器 但是遍历生成器的时候 要按提交任务的顺序,就会阻塞

    # 前面的任务如果好了,就能读出来 但是必须按顺序 后面的即使好了,也要等前面好了才能读到结果
    for r in results:
        print(r)
    # map 本身不是阻塞的,但是要得到map出来的东西,那就是阻塞的

    executor.shutdown(wait=True)




