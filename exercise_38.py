#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:34:50 2020

@author: henry
"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')

more_stuff = ["day", 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"here are {len(stuff)} items now.")
    
print("There we go: ", stuff)
print("Let's do some things with stuff.")
    
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print("all stuff", stuff)
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
    