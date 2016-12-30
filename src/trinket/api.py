from src.trinket.server import trinketserver
import socket
class serverapi():

    @staticmethod
    def start():
        global server
        server = trinketserver.init(ip=socket.gethostbyname(socket.gethostname()),port=26625)



