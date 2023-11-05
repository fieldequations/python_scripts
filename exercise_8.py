#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:16:51 2020

@author: henry
"""

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format(True,1,'qwe',formatter.format(1,2,6,44)))