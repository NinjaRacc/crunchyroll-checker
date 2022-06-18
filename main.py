#!/usr/bin/env python3
"""
 _   _ _        _       ____                
 | \ | (_)_ __  (_) __ _|  _ \ __ _  ___ ___ 
 |  \| | | '_ \ | |/ _` | |_) / _` |/ __/ __|
 | |\  | | | | || | (_| |  _ < (_| | (_| (__ 
 |_| \_|_|_| |_|/ |\__,_|_| \_\__,_|\___\___|
              |__/                           
"""

### Importing
# Importing Inbuilt-Packages
import os

# Importing Dev Defined Script
import src.checker

tag = """
  __  __           _        ____          _   _ _        _       ____                
 |  \/  | __ _  __| | ___  | __ ) _   _  | \ | (_)_ __  (_) __ _|  _ \ __ _  ___ ___ 
 | |\/| |/ _` |/ _` |/ _ \ |  _ \| | | | |  \| | | '_ \ | |/ _` | |_) / _` |/ __/ __|
 | |  | | (_| | (_| |  __/ | |_) | |_| | | |\  | | | | || | (_| |  _ < (_| | (_| (__   (not really mostly skidded)
 |_|  |_|\__,_|\__,_|\___| |____/ \__, | |_| \_|_|_| |_|/ |\__,_|_| \_\__,_|\___\___|
                                  |___/               |__/                           
"""

def main():
    print(tag)
    if not os.path.exists('result'):
        os.makedirs('result')
        
    filename = input("Enter the name or path of file: ")
    if os.path.isfile(filename):
        src.checker.CrunchyrollChecker.create(filename)
    else:
        print("File not found.")


### yeaaahhhh!!!!
if __name__ == "__main__":
    main()

