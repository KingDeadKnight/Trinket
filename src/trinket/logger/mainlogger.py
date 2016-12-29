from trinket.utils import textformat

class mainlogger(object):

    def __init__(self):
        print('\x1b[1;34;40m' + "[" + "] " + '\x1b[1;32;40m' + "[MainLogger/INFO] Starting up..." + '\033[0m')


    @staticmethod
    def warning(self,  message):
        print('\x1b[1;34;40m' + "[" + "] " + '\x1b[1;31;40m'+ "[MainLogger/WARNING] " + message + '\033[0m')
