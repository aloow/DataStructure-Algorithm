# encoding: utf-8
from threading import Thread,Lock,RLock
import time

mutexA=RLock()
mutexB=Lock()
# mutexB=mutexA=RLock()


class Mythead(Thread):
    def run(self):
        self.f1()
#        self.f2()

    def f1(self):
        mutexA.acquire()
        print('%s 抢到A锁' %self.name)
        print('再次加锁前')
        mutexA.acquire()
        print('再次加锁后')
        mutexB.acquire()
        print('%s 抢到B锁' %self.name)
        mutexB.release()
        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print('%s 抢到了B锁' %self.name)
        time.sleep(2)
        mutexA.acquire()
        print('%s 抢到了A锁' %self.name)
        mutexA.release()
        mutexB.release()


    
def main():

    t=Mythead()
    t.start()
 
 
 
    
if __name__ == "__main__":
    main()


