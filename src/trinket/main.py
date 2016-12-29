# Trinket.py
""""
  _______   _       _        _    
 |__   __| (_)     | |      | |   
    | |_ __ _ _ __ | | _____| |_  
    | | '__| | '_ \| |/ / _ \ __| 
    | | |  | | | | |   <  __/ |_  
    |_|_|  |_|_| |_|_|\_\___|\__| 
                                                             
"""
import time
import _thread
from queue import Queue
from time import sleep
import sys
import socket
import ctypes

from trinket.logger import mainlogger
from trinket.thread import consolethread
import _thread


class main():

    def __init__(self):

        global MAX_STARTTIME
        self.MAX_STARTTIME = 60000
        global MAX_SHUTDOWN_TIME
        self.MAX_SHUTDOWN_TIME = 30000
        global THREADS
        self.THREADS = []
        global CLIENTS
        self.CLIENTS = []
        global STARTTIME
        self.STARTTIME = int(round(time.time() * 1000))
        global QUEUE
        self.QUEUE = Queue()
        global MAXPLAYERS
        self.MAXPLAYERS = 20
        global NAME
        self.NAME = "Trinket"
        global VERSION
        self.VERSION = "0.0.2-BETA"
  
    def timecheck():
        while True:
            TIME = self.STARTTIME - int(round(time.time() * 1000))
            if TIME > self.MAX_STARTTIME:
                mainlogger.warning("Startup exceeded maximum startup time!")
            for thread in THREADS:
                thread.Thread_Stop()
            sys.exit(1)
        
    def setWindowName():
        while True:
            ctypes.windll.kernel32.SetConsoleTitleA("Trinket-" + self.VERSION + " | Online " + str(self.CLIENTS.count()) + "/" + str(self.MAXPLAYERS) + " | @ " + Thread.activeCount() + " threads")
  
    if sys.version_info < (3,3):
        mainlogger.warning("Please update Python to 3.3")
        sys.exit(1)
    
    _thread.start_new_thread(timecheck, ())
    consolethread.__init__("ConsoleThread")
  
  
  
  
  
  
  
