import queue
import random
import threading
import time

#生产者线程
lock = threading.Lock()
class Producer(threading.Thread):
    def __init__(self, t_name, aqueue):
        threading.Thread.__init__(self, name=t_name)
        self.data=aqueue
    def run(self):
        for i in range(10):
            lock.acquire()
            print ("%s: %s is producing %d to the queue!" %(time.ctime(), self.getName(), i))
            self.data.append(i)# put(i)  # 将生产的数据放入队列
            lock.release()
            time.sleep(2)
        print ("%s: %s finished!" %(time.ctime(), self.getName()))

#消费者线程
class Consumer(threading.Thread):
    def __init__(self, t_name, aqueue):
        threading.Thread.__init__(self, name=t_name)
        self.data=aqueue
    def run(self):
        for i in range(10):
            lock.acquire()
            try:
                if len(self.data) > 0:
                    val = self.data.pop(0)#get()  # 拿出已经生产好的数据
                    #self.data.task_done() # 告诉队列有关这个数据的任务已经处理完成
                    print ("%s: %s is consuming. %d in the queue is consumed!" %(time.ctime(), self.getName(), val))
            except queue.Empty:
                print('queue.Empty')
            lock.release()
            time.sleep(2)
        print ("%s: %s finished!" %(time.ctime(), self.getName()))

#主线程
def main():
    tqueue = []#queue.SimpleQueue()
    
    producer = Producer('Pro.', tqueue)
    consumer = Consumer('Con.', tqueue)
    #queue本身是线程安全的，put,get 会阻塞，不需要用到thread.Lock()
    producer.start()
    consumer.start()
    
    producer.join() # 等待生产者线程结束
    consumer.join() # 等待消费者线程结束
    #queue.join()  # 阻塞，直到生产者生产的数据全都被消费掉
    print ('All threads terminate!')
 
if __name__ == '__main__':
    main()