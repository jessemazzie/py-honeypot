from socket import socket, AF_INET, SOCK_STREAM
import sys

#Main function. Controls general program flow.
def main():
	if len(sys.argv) != 2:
		print('No port number supplied.')
		exit()
	else:
		print('Starting...')
		openPort(sys.argv[1]) #strip first element from sys.argv, because that is the program name.

#Exits program
def exit():
	print('Exiting...')
	sys.exit()

#Listens on a given port.
def openPort(port):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		port = int(port)
		print(port)
	
		sock.bind(('127.0.0.1', port))
	
		sock.listen()
			
		while True:
			connection, client_addr = sock.accept()
			print(connection)
			
			print(client_addr)
    
	except TypeError:
		print('Invalid arguments. Argument must be integer in range: 0-65535.')

#Used for appending access logs to end of log file.
def log(text_to_log):
	with open("honeypot.log") as f:
		f.write(text_to_log)

#enter main program loop.
main()