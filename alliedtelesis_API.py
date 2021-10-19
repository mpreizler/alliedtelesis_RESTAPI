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
    os.system('cls')
    return(switch)

# headers
payload={}

# This function allows to select different options for API REST

def get_option():
    print("\nPlease select to gather information from AlliedWare Plus Operating system\n\n")
    print("1: View all your system status\n")
    print("2: View interfaces\n")
    print("3: Get interfaces details\n")
    print("4: Get vlan1 information\n")
    r = str(input("Your option is: "))
    return(r)

# This function prints the results

def print_info(x):
    result=json.loads(x)
    pprint.pprint(result)

def aw(name_switch):
    print("Please enter username of the switch:")
    user = input()
    print("Please enter password of the switch:")
    pwd = input()
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
    print("Your switch is {} username: {} password: {}".format(name_switch,user,pwd))
    print("Is it correct?(y/n)\n")
    rta=input()
    if rta == "n":
        quit()
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
    print('\033[0;36;40m"Welcome to Allied Telesis API Programmability"')
    name_switch=switch_selection()
    while answer == "n":
        # clean screen from OS function
        #os.system('clear')
        aw(name_switch)
        print("\nWould you like to exit from network programmability software (Press y to exit)?\n")
        answer = input()
    print("\nThanks for using our Allied Telesis switches with REST API\n")
