import sys
import subprocess
import pkg_resources
from keyboard import press_and_release, write
from time import sleep


def install(): 
    package_name = input("What is the package called u want to install ?: \n").lower().strip()
    if package_name in sys.modules:
      print(f"{package_name!r} already in sys.modules")
      exit()
    else:
        print(f"Looks like {package_name!r} is not installed on your device")
        Action = input("Install? (y/n): \n").lower().strip()
        if Action == "y":
          subprocess.check_call ( [ sys.executable, '-m', 'pip', 'install', package_name ]  )
          Antwort = input("Do you want to execute it again? (y/n): \n").lower().strip()
          if Antwort == "y":
            write(f'pip show {package_name}')
            press_and_release('enter')
            write('python command.py')
            sleep(0.1)
            press_and_release('enter')
          if Antwort == "n":
            write(f'pip show {package_name}')
            press_and_release('enter')
            exit()
        if Action == "n":
          write('exit')
          sleep(0.1)
          press_and_release('enter')