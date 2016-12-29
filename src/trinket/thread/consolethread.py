#!/usr/bin/python3
from threading import Thread
import time
import sys
from src.trinket.command import commandreader

class ConsoleThread(Thread):
  
  def __init__(id, name):
    Thread.start_new_thread(commandchecker, (,))
  
  def commandchecker():
    while True:
      cmd = input("")
      commandreader.read(cmd)
      
