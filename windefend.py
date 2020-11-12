import sys
import os
from elevate import elevate


if __name__ == "__main__":
    elevate()
    args = sys.argv[1]
    if args == "disable":
        os.system("windefend-disable.bat")
    elif args == "enable":
        os.system("windefend-enable.bat")
    else:
        print(
            "Run the script again with correct arguments (windefend.py disable or windefend.py enable")
