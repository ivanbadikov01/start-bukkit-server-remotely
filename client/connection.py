import socket

HOST = '31.13.255.6'
PORT = 56604

def start_server():
	global data, HOST, PORT
	flag = bytes([1])
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(flag)
		data = s.recv(1024)

def get_label_text():
	global data
	return data

def initialize_label() :
	global HOST, PORT
	flag = bytes([2])
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		s.sendall(flag)
		return s.recv(1024)