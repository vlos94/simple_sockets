import socket
import AddressParser
import threading
import sys
import signal

##Clean up and exit after receiving a SIGINT
def sigint_handle(sig_num, frame):
    listen_sock.close()
    print("\nGoodbye!\n")
    sys.exit(0)

##Handle the input from a connected socket
def sock_handle(conn_sock):
    message_chunks = []
    chunk = conn_sock.recv(256)
    ##Get the input from the socket
    while chunk:
        message_chunks.append(chunk.decode())
        chunk = conn_sock.recv(256)
    
    message = ''.join(message_chunks)
    ##Acquire lock, write message, & release lock
    lock.acquire()
    sys.stdout.write(message)
    sys.stdout.flush()
    lock.release()

    conn_sock.close()

parser = AddressParser.AddressParser()

##Get an address to bind a socket to
address = parser.parse_address()

##Use a lock so that a thread can write
##its message to the stdout from start to end
lock = threading.Lock()

##Install the signal handler
signal.signal(signal.SIGINT, sigint_handle)

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    listen_sock.bind(address)
except Exception as e:
    print('Socket bind failed:\n{}'.format(e))
    
listen_sock.listen()
    
while True:    
    conn_sock, _ = listen_sock.accept()
    
    worker = threading.Thread(target=sock_handle, args=(conn_sock,))
    worker.run()


