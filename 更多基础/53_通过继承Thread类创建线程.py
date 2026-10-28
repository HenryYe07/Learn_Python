import os
import time
from multiprocessing import Process
from threading import get_native_id,Thread,RLock

class SpeakThread(Thread):
    def __init__(self,lock,**kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(10):
            self.lock.acquire()
            print(index, "我在说话", "pid:", os.getpid(), "线程的编号是", get_native_id())
            self.lock.release()
            time.sleep(1)


class StudyThread(Thread):
    def __init__(self,lock,**kwargs):
        super().__init__(**kwargs)
        self.lock = lock

    def run(self):
        for index in range(10):
            self.lock.acquire()
            print(index, "我在说话", "pid:", os.getpid(), "线程的编号是", get_native_id())
            self.lock.release()
            time.sleep(1)



if __name__ == "__main__":
    print("---start---","pid是",os.getpid(),"线程是",get_native_id())
    lock = RLock() # 也有RLock确保原子性
    t1 = SpeakThread(lock)
    t2 = SpeakThread(lock)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("---end---")






