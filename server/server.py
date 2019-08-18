import subprocess
import socket
from pprint import pprint

is_running = False
status = b'Server is not running'

def write_to_log():
	global addr, status
	log = open('log.txt', 'a')
	address = ''.join( str(addr).split() )
	output = "Connected by: " + address + " Server status: " + str(status)
	log.write(output + "\n")
	log.close()
	print(output)

def start_server():
	batch_path = "C:\\Users\\aiwan\\Desktop\\mc-server\\run.bat"
	return subprocess.Popen(batch_path, creationflags=subprocess.CREATE_NEW_CONSOLE)

HOST = '192.168.0.104'
PORT = 56604

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
			flag = conn.recv(1024) 
			print(flag)
			if flag == bytes([2]):
				conn.sendall(status)
			elif flag == bytes([1]) :
				if is_running == True and p.poll() == None:
					status = b'Server is running.'
				elif is_running == False:
					p = start_server()
					is_running = True
					status = b'Starting the server...'	
				elif is_running == True and p.poll() != None:
					is_running = False		
				conn.sendall(status)
				write_to_log()
