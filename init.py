from colorama import Fore, Style, init
from os import remove
from sys import platform
from main import error, is_configurated, check_dependencies, warning

init(autoreset=True)

def auto_delete():
  remove('init.py')

def create_scripts_linux():
  pass

def register_to_path_linux():
  pass

def create_scripts_windows():
  pass

def register_to_path_windows():
  pass

def prepare_scripts():
  if platform.startswith('linux'):
    create_scripts_linux()
    register_to_path_linux()
  elif platform == 'win32' or platform == 'cygwin':
    create_scripts_windows()
    register_to_path_windows()
  else:
    error("Your platform is not supported. Feel free to send a PR!")

if __name__ == '__main__':
  if is_configurated():
    warning('Application already configured, deleting this script...')
    auto_delete()
  else:
    check_dependencies()
    prepare_scripts()