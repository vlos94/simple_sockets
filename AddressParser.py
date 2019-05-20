import argparse


'''Simple class for arg parsing in the
  client and server. Basically just wraps a pre-made parser'''
class AddressParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser('get an port num and host name')
        self._parser.add_argument('-host', type=str)
        self._parser.add_argument('-port', type=int)
        
    '''Parse the args and provide an (hostname, port_num)
       tuple for use with sockets'''
    def parse_address(self):
        try:
            names = self._parser.parse_args()
        except Exception as e:
            print('Address parse failed:\n{}'.format(e))
        
        address = (names.host, names.port)
        return address
