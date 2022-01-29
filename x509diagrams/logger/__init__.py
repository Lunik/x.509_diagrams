
import logging
from colorama import init, Fore, Back, Style


init(autoreset=True)

class ColorFormatter(logging.Formatter):
  COLORS = {
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "DEBUG": Fore.BLUE,
    "INFO": Fore.GREEN,
    "CRITICAL": Fore.RED + Back.WHITE,
  }

  def format(self, record):
    color = self.COLORS.get(record.levelname, Fore.WHITE)

    record.name = record.name.split('.')[-1]

    record.name = Fore.MAGENTA + record.name + Style.RESET_ALL
    record.levelname = Style.BRIGHT + color + record.levelname + Style.RESET_ALL
    record.msg = color + record.msg + Style.RESET_ALL

    return logging.Formatter.format(self, record)


class ColorLogger(logging.Logger):
  def __init__(self, name):
    logging.Logger.__init__(self, name)
    color_formatter = ColorFormatter("%(levelname)s\t- %(message)s")
    console = logging.StreamHandler()
    console.setFormatter(color_formatter)
    self.addHandler(console)


def get_custom_logger():
  logging.setLoggerClass(ColorLogger)

  return logging.getLogger()