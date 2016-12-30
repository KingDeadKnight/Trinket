class trinketserver():
    @staticmethod
    def init(ip, port, version = '1.0.0'):
        global interface
        interface = trinketinterface.init(ip= ip, port= port, version= version)

class trinketinterface():
    @staticmethod
    def init(ip, port = 26625, version = '1.0.0'):
        global sckt
        sckt = udpinterface.init(ip= ip, port= port)
        if not sckt:
            return False
        else:
            return True

from threading import Thread
import socket
import sys
class udpinterface():
    @staticmethod
    def listen():
        while True:
            try:
                s.listen(1)
                data, addr = s.accept()
                print("connection!")
                d = s.recv(65536)
                print(str(d))
            except socket.error:
                print('\033[91m' + '[Trinket/ERROR] ' + 'Error Listening to Port ')
                print('\033[91m' + '[Trinket/ERROR] ' + 'Server Forcefully Stopping...')
                s.shutdown(1)
                t._stop()


    @staticmethod
    def init(ip, port = 26625):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.SOL_UDP)
        try:
            s.bind((ip, port))
        except socket.error:
            print('\033[91m' + '[Trinket/ERROR] ' + "Unable to bind to target host")
            sys.exit(1)
        print( '[Trinket/INFO] '+ "Binded to " + str(ip) + ":" + str(port))
        global t
        t = Thread(target=udpinterface.listen, args=0)
        t.setDaemon(True)
        try:
            while True:
                continue #keeps script alive
        except KeyboardInterrupt:
            sys.exit(1)

