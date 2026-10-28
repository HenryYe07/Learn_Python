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

    # 调用三次work 得到三个协程对象
    # 这并不会引起代码执行
    coroutine1 = work(1,2)
    coroutine2 = work(3,2)
    coroutine3 = work(5,2)

    res1 = await coroutine1
    print(res1)

    res2 = await coroutine2
    print(res2)

    res3 = await coroutine3
    print(res3)

    print("main结束了")
    return "main的返回值"


result = asyncio.run(main())
print(result)
