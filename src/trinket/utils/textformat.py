class textformat(object):
    GREEN = '\x1b[1;32;40m'
    RED = '\x1b[1;31;40m'
    AQUA = '\x1b[1;34;40m'
    PURPLE = '\x1b[1;35;40m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    def __init__(self):
        textformat.GREEN = '\x1b[1;32;40m'
        textformat.RED = '\x1b[1;31;40m'
        textformat.AQUA = '\x1b[1;34;40m'
        textformat.PURPLE = '\x1b[1;35;40m'
        textformat.BOLD = '\033[1m'
        textformat.UNDERLINE = '\033[4m'
        textformat.END = '\033[0m'

    def toANSI(self ,text):
        text.replace("§c", textformat.RED)
        text.replace("§4", textformat.RED)
        text.replace("§3", textformat.AQUA)
        text.replace("§b", textformat.AQUA)
        text.replace("§L", textformat.BOLD)
        text.replace("§n", textformat.UNDERLINE)
        text.replace("§d", textformat.PURPLE)
        text.replace("§5", textformat.PURPLE)
        return text + textformat.END
