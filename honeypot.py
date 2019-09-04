from socket import socket, AF_INET, SOCK_STREAM
import sys
import datetime

#Main function. Controls general program flow.
def main():
	if len(sys.argv) != 2:
		print('No port number supplied.')
		exit()
	else:
		print('Starting...')
		openPort(sys.argv[1]) #ignore first element from sys.argv, because that is the program name.

#Exits program
def exit():
	print('Exiting...')
	sys.exit()

#Listens on a given port.
def openPort(port):

	sock = socket(AF_INET, SOCK_STREAM)
	port = port
	log("Listening on port " + port)

	try:
		sock.bind(('127.0.0.1', int(port)))
	except TypeError:
		print('Invalid arguments. Argument must be integer in range: 0-65535.')
		exit()
	
	sock.listen()

	while True:
		connection, client_addr = sock.accept()

		log("Connection made by: " + connection.getpeername()[0]) #first element in peer name is the IP address of the client.

#Used for appending access logs to end of log file.
def log(text_to_log):
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	with open("honeypot.log", "w") as f:
		print("[" + timestamp + "] " + text_to_log)
		f.write("[" + timestamp + "] " + text_to_log)


#enter main program loop.
main()