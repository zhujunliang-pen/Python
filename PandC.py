import threading
import random
import time

# 定义全局变量-账户余额
account_balance = 0
# 创建锁
gLock = threading.Lock()
# 定义生产者线程结束标志
produce_finish = False

# 定义生产者
class Producer(threading.Thread):
    def __init__(self, produce_count, name=''):
        threading.Thread.__init__(self)
        # 设置生产者的生产次数
        self.produce_count = produce_count
        self.name = name

    def run(self) -> None:
        global account_balance
        global produce_finish
        for i in range(self.produce_count):
            gLock.acquire()
            # 每次的工资在0-100中随机产生
            salary = random.randint(0, 100)
            account_balance += salary
            print(
                f'{threading.current_thread().name} produce ${salary}, balance: ${account_balance}')
            gLock.release()
            time.sleep(1)
        print()
        print(f'{threading.current_thread().name} thread end.')

# 定义消费者
class Consumer(threading.Thread):
    def run(self) -> None:
        global account_balance
        # 只要生产者线程没有结束或者还有余额就继续消费
        while account_balance > 0 or not produce_finish:
            gLock.acquire()  # 上锁
            pay = random.randint(0, 100)
            # 如果余额小于支出，则将支出设置为当前余额
            if account_balance < pay:
                pay = account_balance
            account_balance -= pay
            print(f'{threading.current_thread().name} consumes ${pay}, balance: ${account_balance}')
            gLock.release()  # 解锁
            time.sleep(1)
        print()
        print(f'{threading.current_thread().name} thread end.')

def main():
    pro_list = []
    con_list = []
    # 开启2个生产者线程
    for i in range(2):
        th = Producer(produce_count=5, name=f'producer {i}')
        th.start()
        pro_list.append(th)

    # 开启2个消费者线程
    for i in range(2):
        th = Consumer(name=f'consumer {i}')
        th.start()
        con_list.append(th)

    # 等待生产者线程结束
    for i in range(len(pro_list)):
        pro_list[i].join()
    global produce_finish
    produce_finish = True

    # 等待消费者线程结束
    for i in range(len(con_list)):
        con_list[i].join()

if __name__ == '__main__':
    main()
