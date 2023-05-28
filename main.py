# Dadmehr0 - Garfox
import os
import time

from sms_boomber import sms_boomber
from colorama import Fore as c
from setting import (
    INPUT_STRUCT
)
class main:
    commands_help = ['-h','-help']
    def lunch():
        def help():
            print('''Commands\t\t\tUsage\n\nclear\t\t\tfor clear terminal\nexit\t\t\tfor exit script\nstart\t\t\tTo start the script and give information\n''')

        while True:
            terminal = input(" $ ")

            if terminal in commands_help:
                help()
            elif == 'clear'
                os.system('clear' or 'cls')
            elif  == :
        print(c.CYAN + "Please enter your target phonenumber")
        phonenumber = input(c.WHITE + " $ ")

        print(c.CYAN + "Please enter sms number")
        sms_number = input(c.WHITE + " $ ")

        sms_boomber(phonenumber, sms_number)

    def banner():
        os.system("clear" or "cls")

        print(c.GREEN + """
   ___ ___  ___ ___ _    ___ __ _  ___
  (_-</ _ \/ _ `/  ' \  (_-</  ' \(_-< Help: -h,-help
 /___/ .__/\_,_/_/_/_/ /___/_/_/_/___/"""+c.WHITE+"""V 1.6 Rmake Dadmehr0"""+c.GREEN+"""
    /_/""")

        # Sleep time for printing banner as successufly
        time.sleep(3)

if __name__ == "__main__":
    main.banner()
    main.lunch()
