import queue
import sys

#maxsize 设置为小于或等于零，则队列的长度没有限制。
print("simplequeue")
q = queue.SimpleQueue() 
for i in range(3):
    q.put(i)  
for i in range(3):
    print(q.get()) 

print("queue")
q = queue.Queue()
for i in range(4):
    q.put(i)
while not q.empty():
    print(q.get())

print("LifoQueue")
Lq = queue.LifoQueue()
for i in range(4):
    Lq.put(i)
while not Lq.empty():
    print(Lq.get())

print("PriorityQueue")
pq = queue.PriorityQueue()
data = ((2, 'python'), (1, 'lua'), (3, 'js'))
for i in data:
    pq.put(i)
while not pq.empty():
    print(pq.get())

print("test queue.put block=true and except queue.Full")
try:
    q = queue.Queue(2)  # 设置队列上限为2
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-') # 在队列中插入字符串 '-'
    q.put('100', block = True, timeout = 5) # 队列已满，继续在队列中插入字符串 '100'，等待5秒后会引发 queue.Full 异常
except queue.Full:
    print('block=true, and queue.Full')

try:
    q = queue.Queue()
    q.get(block = True, timeout = 5) # 队列为空，往队列中取数据时，等待5秒后会引发 queue.Empty 异常
except queue.Empty:
    print('get block=true, queue.Empty')

try:
    q = queue.Queue()
    q.get_nowait() # 队列为空，往队列中取数据时直接引发 queue.Empty 异常
except queue.Empty:
    print('get_nowait, 不需要block, 直接返回except queue.Empty')
print("-------task_down------------")
q = queue.Queue()
q.put('python')
q.put('-')
q.put('100')
for i in range(3):
    print(q.get())
    q.task_done()  # 如果不执行 task_done，join 会一直处于阻塞状态，等待 task_done 告知它数据的处理已经完成
q.join()