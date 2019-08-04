import subprocess
import socket
from pprint import pprint

is_running = False
status = None

def write_to_log():
	global addr, status
	log = open('log.txt', 'a')
	address = ''.join( str(addr).split() )
	output = "Connected by: " + address + " Server status: " + str(status)
	log.write(output + "\n")
	log.close()
	print(output)

HOST = '192.168.0.104'
PORT = 56604

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
			if is_running == True and p.poll() == None:
				status = b'Server is running.'
			elif is_running == False:
				batch_path = "C:\\Users\\aiwan\\Desktop\\mc-server\\run.bat"
				p = subprocess.Popen(batch_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
				is_running = True
				status = b'Starting the server...'	
			elif is_running == True and p.poll() != None:
				is_running = False		
			conn.sendall(status)
			write_to_log()
