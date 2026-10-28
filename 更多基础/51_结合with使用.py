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
    with ProcessPoolExecutor(max_workers=3) as executor:

        results = executor.map(work,[1,2,3,4,5,6,7])

        print(list(results))
    print("代码执行完成")
    # 出这个代码块会自动shutdown 并且 wait是true




