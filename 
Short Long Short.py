#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:16:27 2021

@author: yamamotod
"""

#Given 2 strings, a and b, return a string of the form short+long+short, 
#with the shorter string on the outside and the longer string on the inside. 
#The strings will not be the same length, but they may be empty ( zero length ).
def solution(a, b):
    if len(a) < len(b):
        return(a + b + a)
    else:
        return(b + a + b)

print(solution('U','False'))


def solution(a, b):
    return '{0}{1}{0}'.format(*sorted((a, b), key=len))