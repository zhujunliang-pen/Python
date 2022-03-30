import smtplib, sys, os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formataddr

def sendmail_local(): 
	sender = 'from@runoob.com'
	receivers = ['zhujunliang_pen@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
	# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
	message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
	message['From'] = Header("菜鸟教程", 'utf-8')     # 发送者
	message['To'] =  Header("测试", 'utf-8')          # 接收者
 
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8')
	try:
		smtpObj = smtplib.SMTP('localhost')
		smtpObj.sendmail(sender, receivers, message.as_string())
		print ("邮件发送成功")
	except smtplib.SMTPException:
		print ("Error: 无法发送邮件")

def sendmail_third():
	# 第三方 SMTP 服务
	
	mail_host="smtp.163.com"  #设置服务器
	mail_user="zhujunliang_pen"    #用户名
	mail_pass="billsha221007"   #口令 	
	sender='zhujunliang_pen@163.com'
	receivers = ['zhujunliang_pen@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	
	message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
 
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8')
 
	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		
		smtpObj.login(mail_user,mail_pass)
	
		smtpObj.sendmail(sender, receivers, message.as_string())
	
		print ("邮件发送成功")
	except smtplib.SMTPException:
		print ("Error: 无法发送邮件")

def sendhtmlmail_third():
	mail_host="smtp.163.com"  #设置服务器
	mail_user="zhujunliang_pen"    #用户名
	mail_pass="billsha221007"   #口令 
	sender = 'zhujunliang_pen@163.com'
	receivers = ['zhujunliang_pen@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	mail_msg = """
	<p>Python 邮件发送测试...</p>
	<p><a href="http://www.runoob.com">这是一个链接</a></p>
	"""
	message = MIMEText(mail_msg, 'html', 'utf-8')
	message['From'] = Header("菜鸟教程", 'utf-8')
	message['To'] =  Header("测试", 'utf-8')
 
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8') 
 
	try:
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print ("邮件发送成功")
	except smtplib.SMTPException:
		print ("Error: 无法发送邮件")
		
def sendhtml_img_attach_mail():
	mail_host="smtp.163.com"  #设置服务器
	mail_user="zhujunliang_pen"    #用户名
	mail_pass="billsha221007"   #口令 
	sender = 'zhujunliang_pen@163.com'
	receivers = ['zhujunliang_pen@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	mail_msg = """
	<p>Python 邮件发送测试...</p>
	<p><a href="http://www.runoob.com">这是一个链接</a></p>
	<p>html插入图片：</p>
	<p><image src='cid:image1'/></p>
	"""
	msgRoot = MIMEMultipart('related')
	msgRoot['From'] = Header("菜鸟教程", 'utf-8')
	msgRoot['To'] =  Header("测试", 'utf-8')
	subject = 'Python SMTP HTML with Image 邮件测试'
	msgRoot['Subject'] = Header(subject, 'utf-8') 
		
	
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)
	msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
	
	p = os.path.dirname(sys.argv[0])
	# 构造附件1，传送当前目录下的 smtp.py 文件
	att1 = MIMEText(open(p + '\\smtp.py', 'rb').read(), 'base64', 'utf-8')
	att1['Content-Type'] = 'application/octet-sream'
	att1['Content-Disposition'] = "attachment; filename=smtp.py"
	msgRoot.attach(att1)
	
	
	# 构造附件2，传送当前目录下的 turtle-star.png 文件
	att2 = MIMEText(open(p + '\\turtle-star.png', 'rb').read(), 'base64', 'utf-8')
	att2['Content-Type'] = 'application/octet-sream'
	att2['Content-Disposition'] = "attachment; filename=turtle-star.png"
	msgRoot.attach(att2)
	
	#插入image
	fp = open(p + '\\turtle-star.png', 'rb')
	msgImage = MIMEImage(fp.read())	
	fp.close()
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)
	try:
		smtpObj = smtplib.SMTP() 
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		#smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
		
		smtpObj.login(mail_user, mail_pass)
		print(msgRoot.as_string())
		smtpObj.sendmail(sender, receivers, msgRoot.as_string())
		print ("邮件发送成功")
	except smtplib.SMTPException:
		print ("Error: 无法发送邮件")
print(sys.argv[1])
if sys.argv[1] == "l":
	sendmail_local()
elif sys.argv[1] == "3t":
	sendmail_third()
elif sys.argv[1] == "3h":
	sendhtmlmail_third()
elif sys.argv[1] == "if":
	sendhtml_img_attach_mail()	