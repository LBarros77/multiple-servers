import socket, time


class SelectorServer:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# sock = socket.socket()
	received_data = ''

	def default_connection(self, host, port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			sock.bind(('localhost', 50002))
		except socket.error as err:
			print(f'Conection default error ocorred: {str(err)}')
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
			sock.sendall(self.received_data.encode('utf-8'))
		sock.close()

	def request(self, host, port):
		self.sock.connect((host, port))
		for number in self.received_data:
			self.sock.send(number.encode('utf-8'))
			time.sleep(2)
		self.sock.close()

	def response(self, host, port):
		print('Initial response.')
		# The next code not functioned
		# self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		try:
			self.sock.bind((host, port))
		except socket.error as err:
			print(f'Response érror ocorred: {err}')
		# self.sock.listen()
		conn, ender = self.sock.accept()
		print('Address: ', ender)
		self.received_data = ''
		while True:
			received_data = conn.recv(1024).decode('utf-8')
			if not received_data:
				conn.close()
				break
			self.received_data += received_data
			time.sleep(2)
			self.sock.send('Ok'.encode('utf-8'))
		self.sock.close()
		print('My datas: ', datas)


if __name__ == '__main__':
	selector = SelectorServer()
	selector.default_connection('127.0.0.8', 5000)

