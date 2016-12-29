from datetime import datetime
class mainlogger():
  
  def warning(message):
    print(textformat.AQUA + "[" datetime.datetime.utcnow() + "] " + textformat.RED + "[MainLogger/WARNING] " + message + textformat.END)
