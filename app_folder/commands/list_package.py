import subprocess
import pkg_resources
from keyboard import press_and_release, write
from time import sleep
from tabulate import tabulate

def list_request():
  global installed_packages
  installed_packages = subprocess.check_output(['pip', 'list']).decode('utf-8')
  installed_packages = installed_packages.strip().split('\n')[2:] 
  packages = [package.split() for package in installed_packages]
  print(tabulate(packages, headers=['Package', 'Version']))

def list():
  Action = input("Do you want to list a installed packages? (y/n) \n").lower().strip()
  if Action == "y":
    list_request()
    Return = input("Do you want to return to main? (y/n) \n").lower().strip()
    sleep(0.3)
    if Return == "y":
      write('python command.py')
      sleep(0.1)
      press_and_release('enter')
    else:
      exit()
  elif Action == "n":
    Return = input("Do you want to return to main? (y/n) \n").lower().strip()
    if Return == "y":
      write('python command.py')
      sleep(0.1)
      press_and_release('enter')
    elif Return == "n":
      list()
    else:
      exit()
  else:
    print('Invalid, try again \n').lower().strip()
    list()