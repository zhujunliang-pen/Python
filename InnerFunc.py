"""
abs()	divmod()	input()	open()	staticmethod()
all()	enumerate()	int()	ord()	str()
any()	eval()	isinstance()	pow()	sum()
basestring()	execfile()	issubclass()	print()	super()
bin()	file()	iter()	property()	tuple()
bool()	filter()	len()	range()	type()
bytearray()	float()	list()	raw_input()	unichr()
callable()	format()	locals()	reduce()	unicode()
chr()	frozenset()	long()	reload()	vars()
classmethod()	getattr()	map()	repr()	xrange()
cmp()	globals()	max()	reverse()	zip()
compile()	hasattr()	memoryview()	round()	__import__()
complex()	hash()	min()	set()	
delattr()	help()	next()	setattr()	
dict()	hex()	object()	slice()	
dir()	id()	oct()	sorted()	exec 内置表达式
"""

print("--all--如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False，相当于all and")
print("all([]),all(())=", all([]))		#空列表,空元组 = true
print("--any--如果iterable的所有元素都为空、0、false，则返回false，如果不都为空、0、false，则返回true。")
print("any([]),any(())=", any([]))		#空列表,空元组 = false

#basestring() 方法是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。
#3.0已转成str
print("isinstance(\"Hello world\", str) = ", isinstance("Hello world", str))
#print("isinstance(\"Hello world\", basestring) = ", isinstance("Hello world", basestring))

#bin() 返回一个整数 int 或者长整数 long int 的二进制表示
print("bin(20)=", bin(20))



num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")