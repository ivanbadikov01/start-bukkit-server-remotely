import subprocess
import socket

is_running = False
status = None

HOST = '192.168.0.104'
PORT = 56604

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		conn, addr = s.accept()
		with conn:
			if is_running == True and p.poll() == None:
				status = b'Server is already running.'
			elif is_running == False:
				batch_path = "C:\\Users\\aiwan\\Desktop\\mc-server\\run.bat"
				p = subprocess.Popen(batch_path, creationflags=subprocess.CREATE_NEW_CONSOLE)
				is_running = True
				status = b'Starting the server...'	
			elif is_running == True and p.poll() != None:
				is_running = False		
			conn.sendall(status)
