import cmath, math
#cmath 复数数学
#math 实数
def isprime(num):
	q = math.sqrt(float(num))	
	#n = int(num ** 0.5)
	n = int(q)
	print(n)
	for i in range(2, n):
		if num % i == 0:
			return False
	return True


print("39 is prime:", isprime(39))	
print("41 is prime:", isprime(41))
print("101 is prime:", isprime(101))		