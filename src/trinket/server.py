from src.trinket.console import commandreader
from threading import Thread
import socket
import sys
import os
class trinketserver():
    global THREADS
    THREADS = list()

    @staticmethod
    def init(ip, port, version = '1.0.0'):
        global interface
        global host
        global binded_port
        global THREADS
        THREADS = list()
        interface = trinketinterface.init(ip= ip, port= port, version= version)
        host = ip
        binded_port = port
        th = Thread(target=commandreader.read, args=0)
        th.setDaemon(True)
        th.start()
        trinketserver.addThread(th)

    @staticmethod
    def getIp():
        return host

    @staticmethod
    def getPort():
        return binded_port

    @staticmethod
    def shutdown(forced = True):
        serverkiller.kill(forced)

    @staticmethod
    def addThread(t):
        THREADS.append(t)

class trinketinterface():
    @staticmethod
    def init(ip, port = 26625, version = '1.0.0'):
        global sckt
        sckt = udpinterface.init(ip= ip, port= port)
        if not sckt:
            return False
        else:
            return True

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
                serverkiller.kill()


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
        trinketserver.addThread(t)
        try:
            while True:
                continue
        except socket.error as msg:
            print('\033[91m' + '[Trinket/ERROR] ' + str(msg))
            serverkiller.kill()

class serverkiller():

    @staticmethod
    def kill(force = True):
        print('\033[91m' + '[Trinket/ERROR] ' + 'Server Forcefully Stopping...')
        os._exit(1)

