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

    # 可以把多个协程对象都丢给事件循环 全部执行完之后 一次拿到所有结果
    result = await asyncio.gather(work(1,2),work(2,2),work(3,2))
    print(result)
    return "main的返回值"


result = asyncio.run(main())
print(result)
