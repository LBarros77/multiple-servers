import socket, time


class SelectorServer:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	received_data = ''

	def default_connection(self, host, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind(('localhost', 50002))
		sock.listen()
		conn, ender = sock.accept()
		while True:
			received = conn.recv(1024).decode('utf-8')
			if not received:
				conn.close()
				break
			self.received_data = received
			self.request(host, port)
			self.response(host, port)
			self.sock.close()
			sock.sendall(self.received_data.encode('utf-8'))
		sock.close()

	def request(self, host, port):
		sock = self.sock
		sock.connect((host, port))
		for number in self.received_data:
			self.sock.send(number.encode('utf-8'))
			time.sleep(2)
		sock.close()

	def response(self, host, port):
		print('Initial response.')
		self.received_data = ''
		sock = self.sock
		sock.bind((host, port))
		self.sock.listen()
		conn, ender = self.sock.accept()
		print('Address: ', ender)
		while True:
			received_data = conn.recv(1024).decode('utf-8')
			if not received_data:
				conn.close()
				break
			self.received_data += received_data
			time.sleep(2)
		sock.close()
		print('My datas: ', datas)


selector = SelectorServer()
selector.default_connection('127.0.0.8', 50002)

