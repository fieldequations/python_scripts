#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:39:02 2020

@author: henry
"""

import sys, os
from sys import argv

#print(os.path)
script, first, second, third = argv

print("script is ",script)
print("next arguments are ",first,second,third)

print(type(first),type(second),type(third))
