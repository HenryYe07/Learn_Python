# 依附主进程的子进程 主进程终止了，这个也会被终止
import os
import time
from multiprocessing import Process

# 一般用来 对主进程
# 后台监控 日志 统计 采样

def monitor():
    while True:
        try:
            with open('../log.txt', 'r') as f:
                lines = sum(1 for _ in f)
        except FileNotFoundError:
            lines = 0
            pass
        print(f"这是守护进程，目前文件有{lines}行")
        time.sleep(1)

def normal():
    while True:
        print("这是平台进程")
        time.sleep(1)


if __name__ == '__main__':
    print(f"我是主进程{os.getpid()}开始")

    p1 = Process(target=monitor,daemon=True)
    # 告诉 Python：主进程正常结束时，不需要等待这个子进程，可以直接终止它。
    p1.start()

    p2 = Process(target=normal)
    p2.start()

    with open('../log.txt', 'a', encoding='utf-8') as f:
        for index in range(10):
            f.write(f"哈哈哈哈哈{index}\n")
            f.flush()
            time.sleep(1)
    print(f"我是主进程{os.getpid()}结束")
    # 执行完开始走销毁流程
    # 先把守护进程关了
    # 如果不是守护进程，主进程会等子进程跑完再关闭自己


    # 如果给守护进程开join，那这个就永远都不会结束了，因为守护是死循环的，在等主

    # 不能在守护进程里创建子进程

