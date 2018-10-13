from colorama import Fore, init, Style

init(autoreset=True)

def success(message):
  print(Fore.GREEN + Style.BRIGHT + message)

def warning(message):
  print(Fore.YELLOW + Style.BRIGHT + message)

def error(message): 
  print(Fore.RED + Style.BRIGHT + message)

def is_configurated():
  return False

def check_dependencies():
  if not got_git():
    error('You must have git installed to be able to download packages')
    exit(1)

def got_git():
  return True