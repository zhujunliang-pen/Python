from operator import index
import threading
import time
import queue
import sys

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, 0.5, self.counter)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:        
        if exitFlag:
            print(f"{threadName}: 中断 ExitFlag = {exitFlag}")
            exit()
        time.sleep(delay)        
        print(f"%s: %s [{counter}]" % (threadName, time.ctime(time.time())))
        counter -= 1

		
class myThread_Lock (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开启线程： " + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁，开启下一个线程
        threadLock.release()

def print_time2(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print (f"%s: %s [{counter}]"% (threadName, time.ctime(time.time())))
        counter -= 1

"""
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
"""
class myThread_Priority(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
		
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)

def process_data(threadName, q):
	global exitFlag
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			data = q.get()
			q.task_done()
			queueLock.release()
			print ("%s processing [%s] exitFlag: %d" % (threadName, data, exitFlag))
		else:
			queueLock.release()
		time.sleep(1)
		print("exitFlag:" + str(exitFlag))
	print(threadName)

class create_Thead(threading.Thread):
	def __init__(self, threadID,name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
		self.index = 1
	def run(self):
		global exitFlag
		print("开启线程:", self.name)
		while not exitFlag:
			queueLock.acquire()
			self.q.put(self.index)
			print(f'{self.name} {self.threadID} add to {self.index}')
			self.index += 1			
			queueLock.release()
			time.sleep(1)
		print("退出线程:", self.name)


def test1():
	# 创建新线程
	thread1 = myThread(1, "Thread-1", 10)
	thread2 = myThread(2, "Thread-2", 10)	
	# 开启新线程
	thread1.start()
	thread2.start()	
	print("2 thread start, 但是运行是乱序")
	time.sleep(4)
	global exitFlag
	exitFlag = 1
	thread1.join()
	thread2.join()
	print ("退出主线程")

threadLock = threading.Lock()	
def test2():
	
	threads = []
	
	# 创建新线程
	thread1 = myThread_Lock(1, "Thread_Lock-1", 1)
	thread2 = myThread_Lock(2, "Thread_Lock-2", 2)
	
	# 开启新线程
	thread1.start()
	thread2.start()
	print("2 thread start, 但是运行是排他的")
	# 添加线程到线程列表
	threads.append(thread1)
	threads.append(thread2)
	
	# 等待所有线程完成
	for t in threads:
		t.join()
	print ("退出主线程")
	
queueLock = threading.Lock()	
workQueue = queue.Queue(10)
def test3():
	threadList = ["Thread-1", "Thread-2", "Thread-3"]
	nameList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven"]
	
	
	threads = []
	threadID = 1
	
	# 创建新线程
	ct = create_Thead(1, 'create_thread1', workQueue)
	ct.start()
	time.sleep(5)

	for tName in threadList:
		thread = myThread_Priority(threadID, tName, workQueue)
		thread.start()
		threads.append(thread)
		threadID += 1

	# 填充队列
	"""queueLock.acquire()
	for word in nameList:
		workQueue.put(word)
	queueLock.release()
	"""	
	# 等待队列清空
	print('add all')
	#while not workQueue.empty():
	#	pass
	time.sleep(10)
	workQueue.join()
	print('added all')
	# 通知线程是时候退出
	global exitFlag 
	exitFlag = 1
	print("exitFlag:" + str(exitFlag))
	# 等待所有线程完成
	for t in threads:
		t.join()
	print ("退出主线程")
if len(sys.argv) == 1:
	exit(0)
if sys.argv[1] == "1":
	test1()
elif sys.argv[1] == "2":
	test2()
elif sys.argv[1] == "3":
	test3()
