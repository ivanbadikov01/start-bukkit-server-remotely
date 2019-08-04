import socket

def start_server():
	global data
	HOST = '31.13.255.6'
	PORT = 56604
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		data = s.recv(1024)

def get_label_text():
	global data
	return data