from trinket.utils import textformat

class mainlogger():

    @staticmethod
    def warning(message):
        print(textformat.AQUA + "[" + "] " + textformat.RED + "[MainLogger/WARNING] " + message + textformat.END)
