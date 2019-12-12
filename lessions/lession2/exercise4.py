#!/usr/bin/env python3

from __future__ import print_function
from pprint import pprint

with open("show_ip_int_brief.txt") as f:
    output = f.readlines()
pprint(output)

int_4 = output[5]
print(int_4)
print(type(int_4))

int_4 = int_4.split()
ip_addr = int_4[1]
intf_name = int_4[0]

print(ip_addr, intf_name)

my_tuple = (intf_name, ip_addr)
print("My Tuple is: ", my_tuple)
