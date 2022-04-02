#string
s = 'Hello World!'
print("--String--")  
print(s)           # 输出完整字符串
print(s[0])        # 输出字符串中的第一个字符
print(s[2:5])      # 输出字符串中第三个至第五个之间的字符串
print(s[2:])       # 输出从第三个字符开始的字符串
print(s * 2)       # 输出字符串两次
print(s + "TEST")  # 输出连接的字符串
print(s[1:10:2])
print('\"hello\nrunoob\"')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print(R'hello\nrunoob')
'''
python字符串格式化符号:

    符   号	描述
      %c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
	  
	  r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
'''
import datetime
import time
from re import S
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))
print("%s=", "{} is {}".format("Today", 6))
print("%s=", "%s is %d"%("Today", 6))  #.format() or %()    格式化字符串
# 以 f开头表示在字符串内支持大括号内的python 表达式
print("f-string 格式化(python表达式)，同%和.format")
name = 'runnoob'
print('Hellow %s %s'%(name, s))
print(f'Hellow {name}')
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')
print(r"f'{1+2}' =", f'{1+2}')

"""
数字	    格式	    输出	     描述
3.1415926	{:.2f}	    3.14	    保留小数点后两位
3.1415926	{:+.2f}	    +3.14	    带符号保留小数点后两位
-1	        {:+.2f}	    -1.00	    带符号保留小数点后两位
2.71828	    {:.0f}	    3	        不带小数
5	        {:0>2d}	    05	        数字补零 (填充左边, 宽度为2)
5	        {:x<4d}	    5xxx	    数字补x (填充右边, 宽度为4)
10	        {:x<4d}	    10xx    	数字补x (填充右边, 宽度为4)
1000000	    {:,}    	1,000,000	以逗号分隔的数字格式
0.25	    {:.2%}	    25.00%	    百分比格式
1000000000	{:.2e}	    1.00e+09	指数记法
13	        {:>10d}	    13	        右对齐 (默认, 宽度为10)
13	        {:<10d}	    13	        左对齐 (宽度为10)
13	        {:^10d}	    13	        中间对齐 (宽度为10)
11	        '{:b}'.format(11)       1011        进制
            '{:d}'.format(11)       11
            '{:o}'.format(11)       13
            '{:x}'.format(11)       b
            '{:#x}'.format(11)      0xb
            '{:#X}'.format(11)	    0XB
"""
t0 = time.time()
time.sleep(1)
name = 'processing'
#f-strings 是指以f或F 开头的字符串，其中以 {}包含的表达式会进行值替换。
#在字符串前加r可防止字符串转义
#u/U:表示unicode字符串
print(f'{name} done in {time.time() - t0:.2f} s')
u =u"我是含有中文字符组成的字符串。"
u8 = u.encode('utf-8')
ugbk = u.encode("GBK")
print(u)
print(u8)
print(ugbk)
print(u8.decode('utf-8'))
bs=b'Hello word'    #只能是ASCII
print(bs)
#列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print("--List--") 
print(list)               # 输出完整列表
print(list[0])            # 输出列表的第一个元素
list[0] = list[0] + "_"
print(list[0])
print(list[1:3])          # 输出第二个至第三个元素 
print(list[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)       # 输出列表两次
print(list + tinylist)    # 打印组合的列表

#大小写转换
str = "www.runoob.com"
print(str.upper())          # 把所有字符中的小写字母转换成大写字母
print(str.lower())          # 把所有字符中的大写字母转换成小写字母
print(str.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str.title())          # 把每个单词的第一个字母转化为大写，其余小写 


#元组用 () 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
print("--Tuple--") 
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第三个的元素 
print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)       # 输出元组两次
print(tuple + tinytuple)   # 打印组合的元组
print(id(tinytuple), id(tuple))

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
knights = {'gallahad': 'the pure', 'robin': 'the brave'} 
print("--Dictionary--")
print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

dict = [[k, v] for k, v in knights.items()]
print(dict)
for k, v in knights.items():
	print(k, v)
	
"""
int(x [,base])	将x转换为一个整数 ,base 为2,8,10,16进制
long(x [,base] )	将x转换为一个长整数
float(x)	将x转换到一个浮点数
complex(real [,imag])	创建一个复数
str(x)		将对象 x 转换为字符串
repr(x)		将对象 x 转换为表达式字符串
eval(str)	用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)	将序列 s 转换为一个元组
list(s)		将序列 s 转换为一个列表
set(s)		转换为可变集合
frozenset(s)	转换为不可变集合
dict(d)		创建一个字典。d 必须是一个序列 (key,value)元组。
chr(x)		将一个整数转换为一个字符
unichr(x)	将一个整数转换为Unicode字符
ord(x)		将一个字符转换为它的整数值
hex(x)		将一个整数转换为一个十六进制字符串
oct(x)		将一个整数转换为一个八进制字符串
"""
a = [1, 2, 3]
b = a[:]
print ("copy list b=a[:]", b)
    
vec = [2, 3, 4, 5, 7]
vec1 = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
print([3 * x for x in vec])
print([3 * x for x in vec if x > 3])
print([[x, 3 * x] for x in vec])
print([[x, y] for x in vec for y in vec1])
print([[vec[i], vec1[i]] for i in range(len(vec))])
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

#使用join链接list成为字符串
params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
print(["%s=%s" % (k, v) for k, v in params.items()])
print(";".join(["%s=%s" % (k, v) for k, v in params.items()]))
#list 分割字符串
s='beiling ; shanghai ; Shenzheng ; Chongqing'
print([k.strip().ljust(10).title() for k in s.split(";")])

print([(round(355/113, i)) for i in range(1, 6)])
print(round(2.6755, 3))
dit = {x: y for x in vec for y in vec1}
print(dit)
for i, v in enumerate(vec1):
	print(i, v)

matrix = [
	[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
list = []
for x in matrix:
	for y in x:
		list.append(y)
print(list)

transposed = []
for i in range(4):
     transposed.append([row[i] for row in matrix])
print(transposed)

print([[row[i] for row in matrix] for i in range(4)])


x = True
y = False
z = False
#not and or
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
