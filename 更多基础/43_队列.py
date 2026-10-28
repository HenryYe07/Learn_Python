# # 先进先出的数据结构
from multiprocessing import Queue,Process # 是可以跨进程的
import time
#
# if __name__ == '__main__':
#     q1 = Queue() # 没参数就是没上限
#
#     q2 = Queue(3) # 最多三个
#
#     q1.put(10)
#     q1.put(20)
#     q1.put(30)
#
#     print(q1.qsize())
#     print(q1.get())
#     print(q1.get())
#     print(q1.get())
#
#     print(q1.empty()) # 是不是空的
#
#     print(q2.full()) # 是不是满的
#
#     q2.put(40)
#     q2.put(50)
#     q2.put_nowait(60) # 不会进入等待状态 满了就抛出异常
#
#
#
#     q2.put(70,timeout=3) # 设置超时 注意 超时是抛出异常 不是就跳过了
#     # 如果超出容量里，新进去的东西会进入等待状态
#     # 等别的地方，把前面的东西get取走了，然后就会进去
#     # 代码会被阻塞住！ 如果不希望阻塞往下看
#
#     q2.put(80,block=False)  # 不阻塞
#
#     # get
#     q2.get()
#     q2.get()
#     q2.get()
#     q2.get() #队列空了去get也会开始等待
#     # 也可以设置timeout 超时了也会报错。
#     # 也有 get_nowait方法 空的就报错
#
#     print("Hi") # 这里暂时是不会出来的

def test(q):
    time.sleep(3)
    result = q.get()
    print("从队列中取出了",result)


if __name__ == '__main__':
    q = Queue(2)
    q.put("Aaa")
    q.put("Bbb")
    print(f"队列是否已满:{q.full()}")


    p1 = Process(target=test,args=(q,))

    p1.start()

    print("即将向已满的队列中添加一个元素 ")
    q.put("Hello")

    print("目前里面的元素有")
    print(q.get())
    print(q.get())