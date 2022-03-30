#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

hw = '你好，\
世界;'
#下面是段落
hw2 = """你好,	
World"""
import sys
 
print("sys.path", sys.path)
print("sys.winver", sys.winver)
print("sys.version", sys.version)
print("sys.version_info", sys.version_info)
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
if True:
	print(hw)
	print(hw2)
	print('这个会打印')
input('按下 enter 键退出，其他任意键显示...\n')  # raw_input  -> input

x = 'runoob'; sys.stdout.write(x + '\n')

x="a"
y="b"
print("换行输出")
print(x)
print(y)

print(x),
print(y),
print('---------')
print("不换行输出")

# 不换行输出
print(x,y)

print("params count:", len(sys.argv), '个参数')
print("params:", str(sys.argv))

a = b = c = 1
a, b, c = 1, 2, "john"

import keyword
print("Python KeyWords:", keyword.kwlist)
for kw in keyword.kwlist:
	print(kw)