#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:19:53 2021

@author: yamamotod
"""


def number(args):
    
    a = ''.join(map(str,args[0:3]))
    b = ''.join(map(str,args[3:6]))
    c = ''.join(map(str,args[7:]))
   
    
   
  
    print(f'"({a}) {b}-{c}"')
number([1,2,3,4,5,6,7,8,9,0])