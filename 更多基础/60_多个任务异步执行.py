# 定义一个协程函数
import asyncio


async def work(n,delay):
    print(f"work{n}开始")
    print(f"work{n}执行中")

    #模拟一个IO等待
    await asyncio.sleep(delay)

    print(f"work{n}结束")

    return f"work的返回值{n}"

async def main():
    print("main开始了")

    # 会把协程对象包装成事件循环调度的任务 也就是Task对象 ,并注册到事件循环中
    task1 = asyncio.create_task(work(1,2))
    task2 = asyncio.create_task(work(2,2))
    task3 = asyncio.create_task(work(3,2))


    res1 = await task1
    print(res1)

    res2 = await task2
    print(res2)

    res3 = await task3
    print(res3)

    print("main结束了")
    return "main的返回值"


result = asyncio.run(main())
print(result)
