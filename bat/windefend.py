from sys import argv
from os import system
from elevate import elevate


if __name__ == "__main__":
    elevate()
    if argv[1] == "disable":
        system("windefend-disable.bat")
    elif argv[1] == "enable":
        system("windefend-enable.bat")
    else:
        print(
            "Run the script again with correct arguments (windefend.py disable or windefend.py enable")
