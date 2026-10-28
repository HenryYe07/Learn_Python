# aio开头的库一般都是支持协程的
import aiohttp
import asyncio

async def download_pic(session,url):
    print(f"开始下载{url}")
    # 发送网络请求,获取图片 发出去后要等服务器返回 等的时间就属于IO等待
    resp = await session.get(url) # 等的是响应的请求头
    # 等待数据 图片很大可能会分多次 要等数据读/下载完
    content = await resp.read() # 等的是完整的请求体

    with open(f"{url[-10:]}","wb") as f:
        f.write(content)

    # 释放连接资源
    await resp.release()

    print("下载完毕")

async def main():
    url_list = [
        "http://www.jxufe.edu.cn/uploadfile/186/202610/93f0163a1b.jpg",
        "http://www.jxufe.edu.cn/uploadfile/186/202610/4af585d8b2.jpg",
        "http://www.jxufe.edu.cn/uploadfile/186/202610/8dd85768d1.jpg"
    ]

    # 创建一个会话对象
    session = aiohttp.ClientSession()

    # 创建多个协程对象
    coroutine_list = [download_pic(session,url) for url in url_list]

    # 把多个协程对象给事件循环
    await asyncio.gather(*coroutine_list) # 等所有任务都完成

    # 关闭会话
    await session.close()

asyncio.run(main())