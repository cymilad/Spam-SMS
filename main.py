from sms_boomber import sms_boomber
from banenr import main_banner
from colorama import Fore as c
from setting import (
    INPUT_STRUCT
)

def main():
    main_banner()

    print(c.CYAN + "Please enter your target phonenumber")
    phonenumber = input(c.WHITE + " $ ")

    print(c.CYAN + "Please enter sms number")
    sms_number = input(c.WHITE + " $ ")

    sms_boomber(phonenumber, sms_number)

main()