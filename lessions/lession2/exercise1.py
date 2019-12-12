#!/usr/bin/env python3

from __future__ import print_function


f = open("./show_version.txt")
output = f.read()

print(output)
print(type(output))
f.close()
print("-" * 100) 

with open("show_version.txt") as f:
    output2 = f.readlines()

print(output2)
print(type(output2))
