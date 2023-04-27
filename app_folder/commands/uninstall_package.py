import sys
import subprocess
from keyboard import press_and_release, write
from time import sleep
import pkg_resources


def uninstall():
    package_name = input("What is the package called u want to uninstall ?: \n").lower().strip()
    if pkg_resources.get_distribution(package_name).version:
      print(f'{package_name} is installed')
      subprocess.call(['pip', 'show', package_name])
      Action = input("Proceed? (y/n): \n")  
      if Action == "y":
        subprocess.check_call ( [ sys.executable, '-m', 'pip', 'uninstall', '-y', package_name ]  )
        print(f"{package_name!r} is uninstalled")
        Antwort = input("Do you want to execute it again? (y/n): \n").lower().strip()
        if Antwort == "y":
          write('python command.py')
          sleep(0.1)
          press_and_release('enter')
          if Antwort == "n":
            exit()
      if Action == "n":
        exit()
    else:
        print('Package not found or installed.')
        write('python command.py')
        sleep(0.1)
        press_and_release('enter')
      
      
      
      