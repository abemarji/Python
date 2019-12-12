#!/usr/bin/env python3

from __future__ import print_function
from pprint import pprint 

with open("show_arp.txt") as f: 
    output = f.readlines()

output = output[1:]
pprint(output) 

output.sort()

output_3 = output[:3]
output_3_joined = "\n".join(output_3) 

with open("arp_entries", mode="wt") as f:
    f.write(output_3_joined)



