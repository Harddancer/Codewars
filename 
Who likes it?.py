#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:06:44 2021

@author: yamamotod
"""


#You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items. 
#We want to create the text that should be displayed next to such an item.

def likes(names):

    l = len(names)
    if  not names:
            return f'no one likes this'
    elif l == 1:
            return f'{names[0]} likes this'
    elif l == 2:
            return f'{names[0]} and {names[1]} like this'
    elif l == 3:
            print(len(names))
            return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
            print(len(names))
            return f'{names[0]}, {names[1]} and {l-2} others like this'

print(likes(["Alex", "Jacob", "Mark"]))