import socket
import json


HOST, PORT = 'localhost', 50002

def _receive_by_server(data):
	HOST_BY_SERVICE = {
		'order': '127.0.0.4',
		'sum': '127.0.0.6',
	}
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_to_server:
		host = HOST_BY_SERVICE[data['service']]
		try:
			sock_to_server.connect((host, PORT))
			sock_to_server.sendall(data['sequence_numbers'].encode('utf-8'))
			content = sock_to_server.recv(1024)
			content = json.loads(content.decode('utf-8'))
			return content
		except Exception as err:
			print(f'Unexpected {err}, {type(err)}')
			raise


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	# Waiting connection from client
	sock.bind((HOST, PORT))
	sock.listen()
	conn, ender = sock.accept()
except (ConnectionRefusedError, OSError) as err:
	print('Verify your connection - ', err)
	sock.close()
finally:
	print('Connected: ', ender)

while True:
	# receive datas and work with this
	received_data = conn.recv(1024)
	if not received_data:
		conn.close()
		break
	data = json.loads(received_data.decode('utf-8'))
	content = _receive_by_server(data)
	content = json.dumps(content)
	conn.sendall(content.encode('utf-8'))

sock.close()
