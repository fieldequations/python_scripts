#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 23:42:09 2020

@author: henry
"""

from sys import argv

script, input_file = argv

def print_all(f):
    for x in range(10):
        #print_a_line(x,f)
        print(get_a_line(f))
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())

def get_a_line(f):
    return f.readline()

current_file = open(input_file)

print("First let's print the first 10 lines of the file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)