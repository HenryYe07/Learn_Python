from multiprocessing import Process,Lock
import os
import time

class SpeakProcess(Process):
    # 如果需要支持传入参数
    def __init__(self,a,b,**kwargs):# 有**kwargs 后面还是可以正常传demon之类的
        super().__init__() # 一定要记得给父类init
        self.a = a
        self.b = b

    def run(self):
        for index in range(5):
            print(f"{self.a}--{self.b}--我在说话{index},进程id是{os.getpid()},父进程是{os.getppid()}")
            time.sleep(1)

class StudyProcess(Process):
    def run(self):
        for index in range(5):
            print(f"我在学习{index},进程id是{os.getpid()},父进程是{os.getppid()}")
            time.sleep(1)

if __name__ == '__main__':


    p1 = SpeakProcess("aa","bb")
    p2 = StudyProcess()



    p1.start() # start会调用对象里面的run函数
    p2.start()