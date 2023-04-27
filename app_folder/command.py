from keyboard import press_and_release, write
from time import sleep
from commands.install_package import install
from commands.uninstall_package import uninstall
from commands.check_package import check
from commands.list_package import list

print("WATCH OUT! Package names with number in them currently arent supported by the check function")
Action = input("Do you want to see the command list? (y/n) \n ").lower().strip()
if Action == "y":
  print("""
        -install (used to install packages) \n
        -unistall (used to uninstall packages) \n 
        -list (used to list all installed packages) \n
        -check (used to check if a package is installed or not) \n
        -exit (just exiting the whole script) \n
        """)
  Action = input("Which function do you want to use ? \n").lower().strip()

elif Action == "install":
    install()
elif Action == "uninstall":
    uninstall()
elif Action == "check":
    check()
elif Action == "list":
    list()
elif Action == "exit":
    exit()
else:
  print('Invalid Input. Try again')
  sleep(0.1)
  write('python command.py') 
  sleep(0.1)
  press_and_release('enter')