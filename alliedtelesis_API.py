"""
A demo to interact with Allied Telesis Operating System: AlliedWare Plus
Author: Mariano Preizler <mariano_preizler@alliedtelesis.com>
alliedtelesis_API.py
Illustrate the following concepts:
- Understanding REST API with Allied Telesis Operating system
"""

__author__ = "Mariano Preizler"
__author_email__ = "mariano_preizler@alliedtelesis.com"
__copyright__ = "Copyright (c) 2021 Allied Telesis, Inc."

# importing some key libraries

import time
import requests
import json
import pprint
import os
import base64


def switch_selection():
    print("\nPlease ingress the IP/name of your switch with AlliedWare Plus Operating system:")
    switch=input()
    return(switch)

# headers
payload={}

# This function allows to select different options for API REST

def get_option():
    while True:
        print("\nPlease select to gather information from AlliedWare Plus Operating system\n\n")
        print("1: View all your system status\n")
        print("2: View interfaces\n")
        print("3: Get interfaces details\n")
        print("4: Get vlan1 information\n")
        r = str(input("Your option is: "))
        if r!="1" and r!="2" and r!="3" and r!="4":
            print("\nYou selected a wrong option\n")
        else:
            break
    return(r)

# This function prints the results

def print_info(x):
    result=json.loads(x)
    pprint.pprint(result)

def aw(name_switch,user,pwd):
    message = user + ":" + pwd
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    headers = {
        'Authorization': 'Basic %s' %base64_message
    }
    url1 = "https://" + name_switch + "/api/system"
    url2 = "https://" + name_switch + "/api/interface"
    url3 = "https://" + name_switch + "/api/interface/interfaces"
    url4 = "https://" + name_switch + "/api/interface/interfaces/vlan1"
    os.system("cls")
    selection = get_option()
    print("\nYou selected option: {}\n".format(selection))
    print("\nLooking for your selection.  Please wait...\n\n")
    time.sleep(1)
    if selection == '1':
        response = requests.get(url1, headers=headers, data=payload, verify=False)
        print_info(response.text)
    elif selection == '2':
        response = requests.get(url2, headers=headers, data=payload, verify=False)
        print_info(response.text)
    elif selection == '3':
        response = requests.get(url3, headers=headers, data=payload, verify=False)
        print_info(response.text)
    elif selection == '4':
        response = requests.get(url4, headers=headers, data=payload, verify=False)
        print_info(response.text)

# Entry point for program
if __name__ == '__main__':
    answer = "n"
    print("\nWelcome to Allied Telesis REST API testing")
    name_switch=switch_selection()
    print("Please enter username of the switch:")
    user_get = input()
    print("Please enter password of the switch:")
    pwd_get = input()
    print("\nYour switch is {} username: {} password: {}".format(name_switch, user_get, pwd_get))
    print("Is it correct?(y/n)")
    rta = input()
    if rta == "n":
        quit()
    while answer == "n":
        aw(name_switch,user_get,pwd_get)
        print("\nWould you like to exit from network programmability software (Press y to exit)?\n")
        answer = input()
        os.system("cls")
    print("\nThanks for using our Allied Telesis switches with REST API\n")
