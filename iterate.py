from re import M
import sys         # 引入 sys 模块

a = 2
b = 3
a, b= b, a+b
print("a={0} b={1}".format(a, b))

list=[1,2,3,4]
print("--iter list--")
it = iter(list)    # 创建迭代器对象
for x in it:
    print(x, end=" ")	
print()	
print("--next--")
for x in list:
    print(x, end=" ")	
print()	

#创建一个迭代器
class MyNumbers:
  def __init__(self, m):
      if m > 0:
        self.max = m
      else:
        self.max = 20

  def __repr__(self) -> str:
      return str(self.max)
  
  def __iter__(self):
    self.a = 1
    return self  
  def __next__(self):
    if self.a <= self.max:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers(22)
print(repr(myclass))
myiter = iter(myclass)

print("__iter__")
for x in myiter:
    print(x, end=" ")	
print()
list = [1,3,2,6,4,9,22,3,4,6]
print("org list:", id(list), list)
sortlist = sorted(list)
print(sortlist)
list.sort()
print('after list.sort:', id(list), list)


def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
print()
print("--yield--fibonacci--")
while True:
	try:
		print (next(f), end=" ")
	except StopIteration:
		break	
	
print()	
list= range(10)
it = iter(list)    # 创建迭代器对象
while True:
	try:
		print (next(it))
	except StopIteration:
		break
print("--fibonacci from import fibonacci-- fibY--")

import Fibonacci
f = Fibonacci.fibY(10)
for x in f:
	print(x, end=",")
print()
from Fibonacci import fibY # from fibo import *
f = fibY(20)
for x in f:
	print(x, end=",")

