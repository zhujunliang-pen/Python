'''
标准数据类型
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
'''


#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。
a, b, c, d = 20, 5.5, True, 4+3j
print("type(a), type(b), type(c), type(d)=", type(a), type(b), type(c), type(d))
print("isinstance(a, int)=", isinstance(a, int))
#在混合计算时，Python会把整型转换成为浮点数。
print("2 / 4=", 2 / 4) # 除法，得到一个浮点数
print("2//4=", 2 // 4) # 除法，得到一个整数
print("17%3=", 17 % 3) # 求余 
print("2**5=", 2 ** 5) # 乘方
num = float(input('用**计算计算平方根： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))
import cmath 
num = int(input("用cmath.sqrt计算计算平方根: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

str = 'Hello World!'
print("--String--")  
print(str)           # 输出完整字符串
print(str[0])        # 输出字符串中的第一个字符
print(str[2:5])      # 输出字符串中第三个至第五个之间的字符串
print(str[2:])       # 输出从第三个字符开始的字符串
print(str * 2)       # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串
print(str[1:10:2])
print('\"hello\n\arunoob\"')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#Set集合
"""parame = {value01,value02,...}
或者
set(value)
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
"""
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam') 
print(a, b)
print(a - b)     # a 和 b 的差集 
print(a | b)     # a 和 b 的并集 
print(a & b)     # a 和 b 的交集 
print(a ^ b)     # a 和 b 中不同时存在的元素

#移除集合中的元素，且如果元素不存在，会发生错误
print(a.remove('a'), a)
a.add('a')
print(a)
print(a.pop())
print(a.pop())
#移除集合中的元素，且如果元素不存在，不会发生错误
print(a.discard('a'), a)
fa = frozenset(range(1,11))
fb = frozenset(range(1,20,2))
#fa.remove(1)
print(fa,fb)
print(fa & fb)
"""
set(可变集合)与frozenset(不可变集合)的区别：
set无序排序且不重复，是可变的，有add（），remove（）等方法。既然是可变的，所以它不存在哈希值。基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交集), difference(差集)和sysmmetric difference(对称差集)等数学运算.
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, 或其它类序列的操作。
frozenset是冻结的集合，它是不可变的，存在哈希值，好处是它可以作为字典的key，也可以作为其它集合的元素。缺点是一旦创建便不能更改，没有add，remove方法。
"""


'''
Set 集合内置方法完整列表
方法	描述
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	删除集合中的元素，该元素在指定的集合中不存在。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
'''

'''
is	is 是判断两个标识符是不是引用自一个对象	x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
is not	is not 是判断两个标识符是不是引用自不同对象	x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
注： id() 函数用于获取对象内存地址。

is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

'''




#Number
'''
数学函数
函数			返回值 ( 描述 )
abs(x)			返回数字的绝对值，如abs(-10) 返回 10
ceil(x)			返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)		如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
exp(x)			返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)			返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)		返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)			如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)		返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)			返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)		x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)			返回数字x的平方根。

随机数函数
随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
函数			描述
choice(seq)		从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()		随机生成下一个实数，它在[0,1)范围内。
seed([x])		改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

三角函数
函数		描述
acos(x)		返回x的反余弦弧度值。
asin(x)		返回x的反正弦弧度值。
atan(x)		返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)		返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)		返回的x弧度的正弦值。
tan(x)		返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度

数学常量
常量	描述
pi		数学常量 pi（圆周率，一般以π来表示）
e		数学常量 e，e即自然常数（自然常数）。
'''
