from colorama import Fore as c
import os
import time

def main_banner():
    os.system("clear" or "cls")

    print(c.GREEN + """
   ___ ___  ___ ___ _    ___ __ _  ___
  (_-</ _ \/ _ `/  ' \  (_-</  ' \(_-<
 /___/ .__/\_,_/_/_/_/ /___/_/_/_/___/
    /_/""" + c.WHITE + "                        V1.5")
    print(" You can exit with Ctrl + C key")

    # Sleep time for printing banner as successufly
    time.sleep(3)