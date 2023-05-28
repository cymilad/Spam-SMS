# Dadmehr0 - Garfox
import os
import time
import platform

from sms_boomber import sms_boomber
from colorama import Fore as c
from colorama import Style as s

commands_help = ['-h','-help']
plat = platform.node()

def banner():
        os.system("clear" or "cls")

        print(c.GREEN + """
   ___ ___  ___ ___ _    ___ __ _  ___
  (_-</ _ \/ _ `/  ' \  (_-</  ' \(_-< """+c.WHITE+"""Help: -h,-help"""+c.GREEN+"""
 /___/ .__/\_,_/_/_/_/ /___/_/_/_/___/ """+c.WHITE+"""V 1.6 Remaked Dadmehr0"""+c.GREEN+"""
    /_/"""+s.RESET_ALL+"""""")

        # Sleep time for printing banner as successufly
        time.sleep(3)

def lunch():
    def info():
        print("""                             
  ___ ___  ___ ___ _    ___ __ _  ___
 (_-</ _ \/ _ `/  ' \  (_-</  ' \(_-<
/___/ .__/\_,_/_/_/_/ /___/_/_/_/___/
   /_/                               

# Sms Spam Iran #
Remastred : Dadmehr0 - Garfox
Creator : Milad Ranjbar
WebSite : CyberAmooz.Com
Telegram : t.me/CyberAmooz
Instagram : instagram.com/CyberAmooz
....................................
""")
    def help():
        print('''Commands\t\t\tUsage\n\nclear\t\t\tfor clear terminal\nexit\t\t\tfor exit script\nstart\t\t\tTo start the script and give information\ninfo\t\t\tGet devlopers information''')

    while True:
        print('['+plat+']-[spam sms]')
        terminal = input(" $ ")

        if terminal in commands_help:
            help()
        elif terminal == 'clear':
            banner()
        elif terminal == 'exit':
            exit()
        elif terminal == 'info':
            info()
        elif terminal == 'start':
            print(c.CYAN + "Please enter your target phonenumber")
            phonenumber = input(c.WHITE + " $ ")

            print(c.CYAN + "Please enter sms number")
            sms_number = input(c.WHITE + " $ ")

            sms_boomber(phonenumber, sms_number)
        else:
            print(c.RED+terminal+": Command not found")


if __name__ == "__main__":
    banner()
    lunch()