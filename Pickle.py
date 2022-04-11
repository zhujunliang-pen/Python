import pickle, os
import json
import datetime 

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

class Person:
	def __init__(self, name, sex, birthday):
		self.name = name
		self.sex = sex
		self.birthday = birthday
		print(self.__class__)		
	def __str__(self):
		return "name: {}, sex: {}, birthday: {}".format(self.name, self.sex, self.birthday)
	
output = open('data.pkl', 'wb')
j = open("data.json", 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)


# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

dt = datetime.datetime(2011, 1, 2)
p = Person("Bill", "M", dt)
pickle.dump(p, output)

output.close()
j.close()
import pprint

#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

obj= pickle.load(pkl_file)
while obj != None:	
	try:
		if obj is Person:
			print(obj.toString())
		else:
			pprint.pprint(obj)
		obj = pickle.load(pkl_file)			
	except EOFError:
		break
#data2 = pickle.load(pkl_file)
#pprint.pprint(data2)

pkl_file.close()

# 打开一个文件
f = open("foo.txt", "w")
f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# 关闭打开的文件
f.close()

print(os.path)
print(os.path.realpath(__file__))    # 当前文件的路径
print(os.path.dirname(os.path.realpath(__file__)))  # 从当前文件路径中获取目录
print(os.path.basename(os.path.realpath(__file__))) # 从当前文件路径中获取文件名

# os.walk()遍历文件夹下的所有文件
# os.walk()获得三组数据(rootdir, dirname,filnames)
def file_path(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root, end=' ')    # 当前目录路径
        #print(dirs, end=' ')    # 当前路径下的所有子目录
        #print(files)            # 当前目录下的所有非目录子文件
file_path("\\")	