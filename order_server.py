import socket
import json


HOST, PORT = '127.0.0.4', 50002

def order(numbers):
	lst = [num for num in str(numbers)] if numbers != list else numbers
	lst.sort()
	num = ''
	for n in lst:
		num += n + ' '
	return num[:-1]


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.bind((HOST, PORT))
	sock.listen()
	conn, ender = sock.accept()
	while True:
		received_data = conn.recv(1024)
		if not received_data:
			conn.close()
			break
		received_data = json.loads(received_data.decode('utf-8'))
		ordered_numbers = order(received_data)
		content = json.dumps(ordered_numbers)
		conn.sendall(content.encode('utf-8'))
	conn.close()
