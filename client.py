import sys
import socket
import AddressParser

parser = AddressParser.AddressParser()

address = parser.parse_address()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    
    try:
        sock.connect(address)
    except Exception as e:
        print('Socket Connection failed:\n{}'.format(e))
        sys.exit(1)
    
    while True:
        line = sys.stdin.readline()
        
        '''A line with only a carriage return
           signals the end of the message
           The terminating char will not be sent'''           
        if len(line) == 1:
            break
        
        sock.send(line.encode())

sock.close()
    
sys.exit(0)





