#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:56:57 2021

@author: yamamotod
"""


#Implement a function that adds two numbers together and returns their sum in binary.
#The conversion can be done before, or after the addition.
#The binary number returned should be a string
def add_binary(a,b):
    return bin(a+b)[2:]
print(add_binary(2,2))


def add_binary(a,b):
    return str("{0:b}".format(a+b))
print(add_binary(2,2))