import asyncio
import time


# 定义一个协程函数
async def work():
    print("工作开始")
    print("正在工作")

    print("工作结束")

    return "工作结果"
# 调用协程函数 会得到协程对象

coroutine  = work() # 调用协程函数并不会执行里面的代码
# 返回的是一个协程对象
print(coroutine)

result = asyncio.run(coroutine) # 会阻塞当前线程 直到完毕 返回return的东西
# 创建了一个事件循环
# 把收到的协程对象 包装成一个任务 交给事件循环
# 启动事件循环
print(result)
