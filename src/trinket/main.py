# Trinket.py
import time
from threaded import Thread
from time import sleep
import sys
import socket
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)

from trinket.utils import textformat
from trinket.logger import mainlogger

  MAX_STARTTIME = 60000
  MAX_SHUTDOWN_TIME = 30000
  THREADS = []
  CLIENTS = []
  
  if sys.version_info < (3,3):
    mainlogger.error("Please update Python to 3.3")
    quit()
  
