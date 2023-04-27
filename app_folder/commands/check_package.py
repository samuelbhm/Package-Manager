import subprocess
import sys
import pkg_resources
from keyboard import press_and_release, write
from time import sleep

def check():
    package_name = input("What is the package called you want to check for?:\n").lower().strip()
    if pkg_resources.get_distribution(package_name).version:
        print(f"{package_name!r} is already installed")
        subprocess.call(['pip', 'show', package_name])
        Action = input('Do you want to return to the main menu? (y/n)\n').lower().strip()
        if Action == 'y':
            write('python command.py')
            sleep(0.1)
            press_and_release('enter')
        if Action == 'n':
            write('exit')
            sleep(0.1)
            press_and_release('enter')
    else:
        print(f"Can't find {package_name!r}")
        action = input(f"Do you want to install {package_name}? (y/n): \n").lower().strip()
        if action == "y":
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(f"{package_name!r} is installed")