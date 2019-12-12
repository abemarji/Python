#!/usr/bin/env python3

from __future__ import print_function

try:
    ip_addr = raw_input("Please enter an IP address: ")
except NameError:
    ip_addr = input("Please enter an IP address: ")


octets = ip_addr.split(".")
octets = [int(octets[0]),int(octets[1]),int(octets[2]),int(octets[3])]

print("{:^15}{:^15}{:^15}{:^15}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(octets[0], octets[1], octets[2], octets[3]))
print("{:^15}{:^15}{:^15}{:^15}".format(bin(octets[0]), bin(octets[1]), bin(octets[2]), bin(octets[3])))
print("{:^15}{:^15}{:^15}{:^15}".format(hex(octets[0]), hex(octets[1]), hex(octets[2]), hex(octets[3])))
print("-" * 60)
print()

