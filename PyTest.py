# 引入日历模块
import calendar

from CF import c_f
print(c_f(1, 35))

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
 
# 显示日历
print(calendar.month(yy,mm))


#Python 最小公倍数算法
def lcm(x, y):
 
   #  获取最大的数
   if x > y:
       greater = x
   else:
       greater = y 
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1 
   return lcm 
# 获取用户输入
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
 
print( num1,"和", num2,"的最小公倍数为", lcm(num1, num2))


#Python 最大公约数算法
def hcf(x, y):
   """该函数返回两个数的最大公约数"""
 
   # 获取最小值
   if x > y:
       smaller = y
   else:
       smaller = x
 
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i 
   return hcf 
# 用户输入两个数字
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
 
print( num1,"和", num2,"的最大公约数为", hcf(num1, num2))

#计算三角形面积
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: ')) 
# 计算半周长
s = (a + b + c) / 2 
# 计算面积
area = float((s*(s-a)*(s-b)*(s-c)) ** 0.5)
#area = cmath.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)
print('三角形面积为 %0.2f' %area)




#Python 判断闰年
year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))
   
