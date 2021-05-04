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
possible = []
possible[:0] = string.printable  # lots of characters here


to_use = possible.copy()  # final string to use

scan = True
again = False

while scan:
    notpossible = []
    notpossible[:0] = input("Enter unwanted elements from the below list:\n\
{}\n".format(possible))  # unwanted ones
    for locn, value in enumerate(notpossible):
        try:
            possible.index("{}".format(value))
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
