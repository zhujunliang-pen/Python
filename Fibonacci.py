# 斐波那契(fibonacci)数列模块
 
def _fib(n):    # 返回n个斐波那契数列
	a, b = 0, 1
	if n<=2:
		return
	i = 1
	while i <= n:
		print(b, end=',')
		a, b = b, a+b
		i += 1
	print()
 
def fib(n):   # 返回n个斐波那契数列
	result = []
	if n <= 2:
		return result
	a, b = 0, 1
	i = 1
	while i <= n:
		result.append(b)
		a, b = b, a+b
		i += 1
	return result

def fibY(n):   # 返回n个斐波那契数列
	#result = []
	#if n <= 2:
	#	return result
	a, b = 0, 1
	i = 1
	while i <= n:
		yield b
		a, b = b, a+b
		i += 1

def recur_fibo(n):
   """递归函数
   输出斐波那契数列"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
	   
#if __name__ == "__main__":
_fib(20)
print(fib(20))
f = fibY(20)
for x in f:
	print(x, end=",")
recur_fibo(20)
