from os import chmod, mkdir, remove, system
from os.path import abspath, exists, expanduser
from sys import platform

from colorama import Fore, Style, init

from main import error, is_configurated, check_dependencies, warning

init(autoreset=True)

def auto_delete():
  remove('init.py')
  remove('init')
  remove('init.bat')

def create_script_file(script, filename):
  if not exists('bin'):
    mkdir('bin')
  with open('bin/{}'.format(filename), 'w') as script_file:
    script_file.write(script) 

def create_scripts_linux():
  script = \
"""#!/bin/bash
cd $GGZYNC_HOME
pipenv run python main.py $@
"""
  create_script_file(script, 'ggz')
  chmod('./bin/ggz', 0o777)

def create_scripts_windows():
  script = \
"""@echo off
cd %GGZYNC_HOME%
pipenv run python main.py %*
"""
  create_script_file(script, 'ggz.bat')

def register_to_path_linux():
  bashrc_path = expanduser('~/.bashrc')
  path_update = 'PATH={}:$PATH\n'.format(abspath('./bin'))
  ggzync_home_export = 'export GGZYNC_HOME=\"{}\"\n'.format(abspath('.'))

  with open(bashrc_path) as path_file:
    path_file_contents = path_file.read()

  def appendLineIfNeeded(): 
    #pylint: disable=used-before-assignment
    if not path_file_contents.endswith('\n'): 
      path_file_contents += '\n'

  if not path_update in path_file_contents:
    appendLineIfNeeded()
    path_file_contents += path_update

  if not 'export GGZYNC_HOME=' in path_file_contents:
    appendLineIfNeeded()
    path_file_contents += ggzync_home_export
  else:
    warning('The GGZYNC_HOME has been set before. Please verify your .bashrc file.')

  with open(bashrc_path, 'w') as path_file:
    path_file.write(path_file_contents)
  
  system('source ~/.bashrc')

def register_to_path_windows():
  from subprocess import run
  from os.path import expandvars

  new_folder = abspath('./bin')
  current_path = expandvars('%PATH%')
  new_path = current_path + new_folder + ';'

  query_string = 'reg:add:HKCU\\Environment:/f:/v:Path:/t:REG_SZ:/d'
  query = query_string.split(':')

  run([*query, new_path], capture_output=True)
  # Broadcast WM_SETTINGCHANGE and set %GGZYNC_HOME%
  run(['setx', '%GGZYNC_HOME%', abspath('.')], capture_output=True)

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
    warning('Application already configured, deleting init scripts...')
  else:
    check_dependencies()
    prepare_scripts()

  auto_delete()