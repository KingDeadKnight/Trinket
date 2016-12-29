# Trinket.py
"""""
  _______   _       _        _    
 |__   __| (_)     | |      | |   
    | |_ __ _ _ __ | | _____| |_  
    | | '__| | '_ \| |/ / _ \ __| 
    | | |  | | | | |   <  __/ |_  
    |_|_|  |_|_| |_|_|\_\___|\__| 
                                                             
""""
import time
from threaded import Thread
from queue import Queue
from time import sleep
import sys
import socket
import ctypes
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

from src.trinket.utils import textformat
from src.trinket.logger import mainlogger

  MAX_STARTTIME = 60000
  MAX_SHUTDOWN_TIME = 30000
  THREADS = []
  CLIENTS = []
  STARTTIME = int(round(time.time() * 1000))
  QUEUE = Queue()
  MAXPLAYERS = 20
  NAME = "Trinket"
  VERSION = "0.0.2-BETA"
  
  def timecheck():
    while True:
      TIME = STARTTIME - int(round(time.time() * 1000))
      if TIME > MAX_STARTTIME:
        mainlogger.error("Startup exceeded maximum startup time!")
        for thread in THREADS:
          thread.Thread_Stop()
        sys.exit(1)
        
  def setWindowName():
    while True:
      ctypes.windll.kernel32.SetConsoleTitleA("Trinket-" + VERSION + " | Online " + CLIENTS.count() + "/" + MAXPLAYERS + " | @ " + Thread.activeCount() + " threads")
  
  if sys.version_info < (3,3):
    mainlogger.error("Please update Python to 3.3")
    sys.exit(1)
    
  Thread.start_new_thread(timecheck, (,))
  
  
  
  
  
  
  
