import os
import sys
import time
os.system("cls")
print(" A project from Devs d`e Nepal (https://devsdenepal.github.io/ , https://github.com/devsdenepal/")
time.sleep(1)
print("Developer : Dev. Gautam Kumar")
print('''
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            CONTROL WLAN IN CLI 
***********************************************
 _______________________________________________
|                                               |
| 1. Show password of prev.connected device     |
| 2. Forgot a device                            |
| 3. Dump all prev.connected device(s)          |
| 4. Show Interface                             |
| 5. Show blocked network                       |
| 6. Show driver(s)                             |
| 7. Show Wireless Capabilities                 |
| 8. Show DNS                                   |
| 9. Show Wlan Profiles                         |
|_______________________________________________|
''')
option = input(" :")
if option == "1" :
 print("The name of  WLAN profile")
 profile_name = input(":")
 statement = "netsh wlan show profile name=" +profile_name + " key=clear"
 os.system(statement)
if option == "2" :
 print("The name of WLAN profile")
 profile_name= input(":")
 statement = "netsh wlan delete profile name=" + profile_name
 os.system(statement)
if option == "3" :
 os.system("netsh wlan show profile")
if option == "4":
 os.system("netsh wlan show interfaces")
if option == "5" :
 os.system("netsh wlan show blockednetwork")
if option == "6":
 os.system("netsh wlan show driver")
if option == "7":
 os.system("netsh wlan show wirelesscapabilities")
if option == "8" :
 os.system("ipconfig /displaydns")
if option =="9":
 os.system("netsh wlan show profile")

