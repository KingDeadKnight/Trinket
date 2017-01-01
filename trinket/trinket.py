from trinket import serverconfig
import os
from pyraklib.server import PyRakLibServer
from pyraklib.server import ServerHandler
from pyraklib.server import ServerInstance
class Trinket():

    def __init__(self, path):
        global config
        #serverconfig.__init__(path)
        #self.port = serverconfig.getData()['port']
        server = PyRakLibServer(26625)
        handler = ServerHandler(server, ServerInstance())
        handler.sendOption("name", "MCCPP;MINECON;TestServer")

