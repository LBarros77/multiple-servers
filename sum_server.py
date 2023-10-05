import socket
import json


HOST, PORT = '127.0.0.6', 50002

def number_sequence_sum(sec_of_numbers):
	# Convert string to integer and return the sum
	numbers_list = map(int, sec_of_numbers)
	return sum(numbers_list)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	sock.bind((HOST, PORT))
	sock.listen()
	conn, ender = sock.accept()
	while True:
		received_data = conn.recv(1024).decode('utf-8')
		if not received_data:
			conn.close()
			break
		data = json.loads(received_data)
		result = number_sequence_sum(received_data)
		result = json.dumps(result)
		conn.sendall(result.encode('utf-8'))
except BaseException as err:
	print('In server from sum has a error: ', err)
finally:
	sock.close()