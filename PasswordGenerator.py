#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:39:25 2020
@author: kivancaykac
purpose:
    random password generator
"""
import random
import string

length = int(input("Length of the password to be generator? "))

password = ""
to_use = []
to_use[:0] = string.printable  # lots of characters here

alphanum = True
while alphanum:
    reply = input("Do you want only alpha-numeric characters?(y/n)\n")
    if reply=='y':
        break
    elif reply=='n':
        alphanum = False
        break
    else:
        print("Please enter either 'y' or 'n'.")
        continue
   
addition = True
while addition:
    reply = input("Do you want to add any possible non-English characters?\
(y/n)\n")
    if reply=='y':
        break
    elif reply=='n':
        addition = False
        break
    else:
        print("Please enter either 'y' or 'n'.")
        continue

unwanted = True
while unwanted:
    print(to_use)
    reply = input("Are there any unwanted characters from the above list?\
(y/n)\n")
    if reply=='y':
        break
    elif reply=='n':
        unwanted = False
        break
    else:
        print("Please enter either 'y' or 'n'.")
        continue

scan = True
again = False
while scan:
    if alphanum:
        to_use = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
                  'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                  'Y', 'Z']
    if addition:
        non_eng = []
        non_eng[:0] = input("Enter the wanted non-English characters.\n")
        to_use += non_eng
    if unwanted:
        notpossible = []
        notpossible[:0] = input("Enter unwanted elements from the below list:\n\
    {}\n".format(to_use))  # unwanted ones
        for locn, value in enumerate(notpossible):
            try:
                to_use.index("{}".format(value))
            except:
                print(value+" is not in the string that was provided.\
    Please enter the unwanted values again.")
                again = True
            else:
                to_use.remove("{}".format(value))
    if again:
        pass  # redo the scan
    else:
        scan = False # finish the scan, onto the generation of the passkey


for i in range(length):
    password += random.choice(to_use)

print("The random password generated:\n{}".format(password))
