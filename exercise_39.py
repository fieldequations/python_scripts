#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 21:16:11 2020

@author: henry
"""

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

cities = {
    'CA':'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['NY'] = 'Albany'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR has: ", cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
#917-224-1922