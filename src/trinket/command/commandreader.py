#!/usr/bin/python3

from src.trinket.utils import textformat
from src.trinket import trinket

class commandreader():
    
    def read(cmd):
      for command in trinket.COMMANDS:
        if cmd == command["name"]:
          
