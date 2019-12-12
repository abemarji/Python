#!/usr/bin/env python3

from __future__ import print_function

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"


fields = mac1.split()
mac1_addr = fields[1]
mac1_mac = fields[3]

fields = mac2.split()
mac2_addr = fields[1]
mac2_mac = fields[3]

fields = mac3.split()
mac3_addr = fields[1]
mac3_mac = fields[3]

print("{:>20}{:>20}".format("IP ADDESS", "MAC ADDRESS"))
print("-" * 20, "-" * 19)
print("{:>20}{:>20}".format(mac1_addr, mac1_mac))
print("{:>20}{:>20}".format(mac2_addr, mac2_mac))
print("{:>20}{:>20}".format(mac3_addr, mac3_mac))
print()
