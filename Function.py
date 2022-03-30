#定义和调用函数必须有()

print("--不定长参数")
def printinfo(arg1, *vartuple):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )
print("--空元组")
printinfo(60)


print("--加了两个星号 ** 的参数会以字典的形式导入。")
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)

print("--单独加*号，*号后面的参数必须是字典输入")
def printinfo_star(a, *, b, c):
   "打印任何传入的参数"
   print ("输出: ")
   print (a + b + c)
   print(b, c)
   
printinfo_star(1, b = 2, c = 3)

print("通过一个元组给一个函数传递四个参数，并且让python将它们解包成不同的参数。")
def func(a,b,c,d):
    print(a,b,c,d)

a = (1,2,3,4)
func(*a)

print("如果已经有一个元祖，在参数前加*，函数会把元祖中的元素一个一个传到函数里面")
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    print(sum)

num = (1,2,3,4)
calc(*num)


print("如果已经有一个dict,在参数前面加**，函数会把dict中所有键值对转换为关键字参数传进去")
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


print("--lambda 来创建匿名函数，必须输入lambda关键字")
sum = lambda arg1, arg2 : arg1 * arg2	

print("sum(2, 3) =", sum(2, 3))
print("sum(5, 6) =", sum(5, 6))
  
print("--全局变量")
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

print("--global 内部作用域想修改全局作用域的变量时")
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = num + 123
    print(num)
fun1()
print(num)

print("--nonlocal 修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量")
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明,调用外部参数
        num = 100
        print("inner\'s out parameter: ", num)
    inner()
    print(num)
outer()
