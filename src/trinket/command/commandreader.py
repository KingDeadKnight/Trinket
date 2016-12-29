#!/usr/bin/python3

from trinket.utils import textformat
from trinket import main

class commandreader():

    @staticmethod
    def read(cmd):
      for command in main.COMMANDS:
        if cmd == command["name"]:
            return True
          
