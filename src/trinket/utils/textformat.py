class textformat():
    def __init__(self):
        global GREEN
        GREEN = '\x1b[1;32;40m'
        global RED
        RED = '\x1b[1;31;40m'
        global AQUA
        AQUA = '\x1b[1;34;40m'
        global PURPLE
        PURPLE = '\x1b[1;35;40m'
        global BOLD
        BOLD = '\033[1m'
        global UNDERLINE
        UNDERLINE = '\033[4m'
        global END
        END = '\033[0m'

    def toANSI(text):
        text.replace("§c", textformat.RED)
        text.replace("§4", textformat.RED)
        text.replace("§3", textformat.AQUA)
        text.replace("§b", textformat.AQUA)
        text.replace("§L", textformat.BOLD)
        text.replace("§n", textformat.UNDERLINE)
        text.replace("§d", textformat.PURPLE)
        text.replace("§5", textformat.PURPLE)
        return text + textformat.END