import socket, time


HOST, PORT = '127.0.0.8', 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.bind((HOST, PORT))
	sock.listen()
	conn, ender = sock.accept()
	datas = list()
	while True:
		received_data = conn.recv(1024)
		if not received_data:
			conn.close()
			break
		datas.append(received_data.decode('utf-8'))
		time.sleep(2)
	print('I am to here!')
	datas.sort()
	for number in datas:
		conn.send(number.encode('utf-8'))
		time.sleep(2)

