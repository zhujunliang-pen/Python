import urllib.request

PI = 3.1415927

def main():
	print("PI:", PI)	
if __name__ == "__main__":
	main()

uo = urllib.request.urlopen('https://www.baidu.com/')
print(uo.read())

myURL1 = urllib.request.urlopen("https://www.runoob.com/")
print(myURL1.getcode())   # 200
'''
https://www.runoob.com/http/http-status-codes.html
HTTP 状态码
200 - 请求成功
301 - 资源（网页等）被永久转移到其它URL
404 - 请求的资源（网页等）不存在
500 - 内部服务器错误
'''
try:
    myURL2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)   # 404

encode_url = urllib.request.quote("https://www.runoob.com/")  # 编码
print(encode_url)