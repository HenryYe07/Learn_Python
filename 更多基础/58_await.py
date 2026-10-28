# 如果 await 后面的代码有IO操作 就会把CPU资源交给事件循环用
# IO 任务执行完毕了会要回来
# await 后面只能写可等待对象 协程对象 Future对象 Task对象

import asyncio

async def work():
    print("工作开始")
    print("正在工作")
    res = await asyncio.sleep(2)
    # 这个时候 事件循环会去看看有没有别的任务
    # 如果有 就切过去 但是在这个项目里,没有别的任务 所以也不会切过去
    print(res)
    print("工作结束")

    return "工作结果"


async def main():
    print("main开始")

    # 运行并等待一个协程对象
    res = await work()

    print("main结束")
    print(res)
    return "main的返回值"
c = main()

result = asyncio.run(c)
print(result)
