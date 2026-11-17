# import functionality 
import functionality as func
# from functionality import welcom_message as wm
# from functionality import *

# functionality.welcom_message()

import menu


func.welcom_message()


while True: 
    try: 
        res = menu.menu()
    except ValueError:
        print("it must be a number ")




    