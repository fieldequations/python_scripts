#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:25:16 2020

@author: henry
"""

tabby_cat = "\tI'm tabbed in"
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\a \\cat"

fat_cat = """
I'll do a list:
\t*one fish
\t*two fish
\t*red fish
\t*blue fish
"""

formatter = "{}\n{}\n{}\n{}"

print(formatter.format(tabby_cat,persian_cat,backslash_cat,fat_cat))