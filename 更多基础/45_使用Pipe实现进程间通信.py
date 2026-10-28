from multiprocessing import Process,Pipe
import time

# 进程1 往队列放数据
def test1(con):
    time.sleep(2)
    con.send(100)
    print("test 1 发送了100")

# 进程2 从队列取数据
def test2(con):
    data = con.recv()
    print("test2 收到了",data)


if __name__ == '__main__':
    con_1,con_2 = Pipe() # 会返回两个对象，也就是管道的两端
    # 默认情况下是双向的，两边都可以发送接收
    # 把 duplex 弄成False 就是单项的 前者只能接收 后者只能发送
    p1 = Process(target=test1,args=(con_1,))
    p2 = Process(target=test2,args=(con_2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()