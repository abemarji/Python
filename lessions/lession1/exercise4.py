#!/usr/bin/env python3

from __future__ import print_function

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    " 
print(show_version)

show_version = show_version.strip()
print(show_version)

field = show_version.split()
model = field[1]
serial_number = field[2]

print ()
vendor_cisco = 'cisco' in model.lower()
print ("Checking if model contains Cisco: {}".format(vendor_cisco))

model_881 = '881' in model
print("Checking if model contains 881: {}".format(model_881))

print("Serial Number: {}".format(serial_number))
print("Model: {}".format(model))
print()


