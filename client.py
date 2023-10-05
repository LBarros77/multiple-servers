import socket
import json


HOST, PORT = '127.0.0.1', 50002

while True:
	try:
		sequence = input('Digite uma sequência de números: ')
		option = input('Escolha 1 para ordenar ou 2 para somar a sequência: ')
		break
	except ValueError:
		print('Oops! That was no valid string or number. Try again...')

options = {'1': 'order', '2': 'sum'}
message = {'sequence_numbers': sequence, 'service': options[f'{option}']}
content = json.dumps(message)

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	try:
		# Connect to server and send data
		sock.connect((HOST, PORT))
		sock.sendall(content.encode('utf-8'))

		# Receive data from the server and shut down
		received_data = sock.recv(1024).decode('utf-8')
		data = json.loads(received_data)
		print('Resultado: ', data)
	except ConnectionRefusedError as err:
		print('Connection refused error: ', err)
	finally:
		print('FINAL')