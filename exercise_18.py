#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 23:37:36 2020

@author: henry
"""

#this one is like argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")
    
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    
#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
    
#this takes no arguments
def print_none():
    print("I got nothing")
    
print_two("led","zepplin", "three")
print_two_again("best","ever")
print_one("runes")
print_none()
