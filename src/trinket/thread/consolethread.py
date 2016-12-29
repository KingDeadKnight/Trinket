#!/usr/bin/python3
import _thread
import time
import sys
from trinket.command import commandreader

class consolethread():
  
    def __init__(self):
      _thread.start_new_thread(commandchecker, ())

    @staticmethod
    def commandchecker(commandreader):
      while True:
        cmd = input("")
        commandreader.read(cmd)
      
