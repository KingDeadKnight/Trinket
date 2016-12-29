# Trinket.py
import time
from threaded import Thread
from queue import Queue
from time import sleep
import sys
import socket
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
  
  def timecheck():
    while True:
      TIME = STARTTIME - int(round(time.time() * 1000))
      if TIME > MAX_STARTTIME:
        mainlogger.error("Startup exceeded maximum startup time!")
        for thread in THREADS:
          thread.Thread_Stop()
        sys.exit(1)
  
  if sys.version_info < (3,3):
    mainlogger.error("Please update Python to 3.3")
    sys.exit(1)
    
  Thread.start_new_thread(timecheck, (,))
  
  
  
  
  
  
  
