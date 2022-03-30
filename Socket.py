import socket, sys, getopt

class socketserver:
	__ss = None
	def __init__(self, port):
		host = socket.gethostname()
		__ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		__ss.bind((host, port))
		__ss.listen(5)
		
		while(True):
			cs, addr = __ss.accept()
			
			print("连接地址:%s" % str(addr))
			msg = "欢迎您"
			cs.send(msg.encode('utf-8'))
			cs.close()

class clientsocket:
	def	__init__(self, port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = socket.gethostname()
		#print(host, port)
		s.connect((host, port))
		msg = s.recv(1024)
		print("收到server的消息:", msg.decode('utf-8'))	
		s.close()		
if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], "s:c:p:", ["server=", "client=", "port="])
		port = 0
		for opt, arg in opts:
			if opt in ("-p", "--port"):
				port = (int(arg))
		print(port)
		for opt, arg in opts:
			if  opt in ("-s", "--server"):
				socketserver(port)
			elif opt in ("-c", "--client"):
				clientsocket(port)				
	except getopt.GetoptError:
		exit()