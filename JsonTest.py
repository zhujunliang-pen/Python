import json
 
# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data)     #对数据进行编码
print("Josn Str", type(json_str))   #对数据进行解码
print ("Python 原始数据：", repr(data))
print ("JSON 对象：", json_str)

# Python 字典类型转换为 JSON 对象
data1 = {
    'no' : 1,
    'name' : 'Runoob',
    'url' : 'http://www.runoob.com'
}
 
json_str = json.dumps(data1)
print ("Python 原始数据：", repr(data1))
print ("JSON 对象：", json_str)
 
# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print ("data2['name']: ", data2['name'])
print ("data2['url']: ", data2['url'])


#如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：
# 写入 JSON 数据
data2 = [1,2,3,'a','b','c',{'data': data}]
with open('data.json', 'w') as f:
    #json.dump(data, f)
    json.dump(data2, f) 
# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)
