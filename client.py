import socket

HOST = '31.13.255.6'
PORT = 56604
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	s.sendall(b'Hello, world!')
	data = s.recv(1024)
	print('Recieved: ', str(data))