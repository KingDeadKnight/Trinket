# Network.py

import socket
from threaded import Thread
import time
import sys
from trinket import serverkiller
from trinket.logger import mainlogger

class Network():
  
  def __init__(s, ip, port, timeout = 3):
    self.start(s, ip, port, timeout)

  
  def start(s, ip '0.0.0.0', port = 19132):
    bind = s.bind(ip, port)
    if not bind:
      time.sleep(timeout)
    
    bind = s.bind(ip, port)
    if not bind:
      mainlogger.error("Unable to bind to " + ip + ":" + port)
      serverkiller.kill(1)
  
      
