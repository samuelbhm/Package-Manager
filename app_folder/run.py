import sys
import subprocess
import importlib.util
from time import sleep

def main():
  from keyboard import press_and_release, write
  press_and_release('win +R')
  sleep(0.1)
  write('cmd')
  sleep(0.1)
  press_and_release('enter')
  sleep(0.1)
  write('color a ')
  sleep(0.1)
  press_and_release('enter')
  sleep(0.1)
  write('G:')  
  sleep(0.1)
  press_and_release('enter')
  sleep(0.1)
  write('cd Final_scripts')  
  sleep(0.1)
  press_and_release('enter')
  sleep(0.1)
  write('cd in_progress')  
  sleep(0.1)
  press_and_release('enter')
  sleep(0.1)
  write('cd app_folder')  
  sleep(0.1)
  press_and_release('enter')
  sleep(0.1)
  write('python command.py')  
  sleep(0.1)
  press_and_release('enter')

packages_to_install = ['keyboard', 'tabulate']
packages_installed = 0

all_packages_imported = True
for package_name in packages_to_install:
    if package_name not in sys.modules:
        all_packages_imported = False
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(f'{package_name} has been installed')
            module = importlib.import_module(package_name)
            sys.modules[package_name] = module
            packages_installed = packages_installed + 1
        except subprocess.CalledProcessError:
            print(f"Failed to install {package_name}")
            all_packages_imported = False

if packages_installed == 2:
  main()
