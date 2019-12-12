#!/usr/bin/env python3

from __future__ import print_function


ip_list = ["1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4", "5.5.5.5"]
print(ip_list) 

ip_list.append("6.6.6.6")
print(ip_list)

ip_list.extend(["7.7.7.7", "8.8.8.8"])
print(ip_list)
ip_list = ip_list + ["9.9.9.9", "10.10.10.10"]

print()
print(ip_list) 

print("Printing First and Last Element of the list: ")
print(ip_list[0])
print(ip_list[-1])

print("POP first element: ")
ip_list.pop(0)
print(ip_list) 

print("POP Last element: ")
ip_list.pop()
print(ip_list)

print("Changing First Element to 2.2.2.2: ")
ip_list[0] = "2.2.2.2"
print(ip_list) 

