#!/usr/bin/env python3

from __future__ import print_function

with open("show_ip_bgp_summ.txt") as f:
    output = f.readlines()

#print(output)

line_1 = output[0].split()
line_2 = output[-1].split()

as_num = line_1[-1]
peer_ip = line_2[0]

print("Local AS Number:", as_num)
print("BGP Peer IP: ", peer_ip)


