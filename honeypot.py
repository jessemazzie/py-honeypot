import socket
import sys



#Main function. Controls general program flow.
def main():
    if len(sys.argv) != 2:
        print('No port number supplied.')
        exit()
    else:
        print('Starting...')
        openPort(sys.argv[1]) #strip first element from sys.argv, because that is the program name.



def exit():
    print('Exiting...')
    sys.exit()

def openPort(port):
    try:
        port = int(port)
        print(port)
    except TypeError:
        print('Invalid arguments. Argument must be integer in range: 0-65535.')

main()