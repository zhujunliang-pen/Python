import sys

print(__name__, __import__, sys.argv)
print()

#列表推导
names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
name1 = [name.upper() for name in names if len(name)>3]
print(';'.join(name1))

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

#字典推导
listdemo = ['Google','Runoob', 'Taobao', '百度']
newdict = {key:len(key) for key in listdemo}
print(newdict)

dic = {x: x**2 for x in (2, 4, 6)}
print(dic)

#集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

#元组推导,结果是 <generator object <genexpr> at 0x7feb50831d60> 生成器对象，要tuple(t)
t = (x for x in range(1,20) if x > 2)
print(tuple(t))

