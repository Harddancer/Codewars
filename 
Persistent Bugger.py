#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:02:08 2021

@author: yamamotod
"""
#Write a function, persistence, that takes in a positive parameter num
# and returns its multiplicative persistence, which is the number 
#of times you must multiply the digits in num until you reach a single digit

def persistence(n):
    count = 0
    while True:
        if len(str(n)) == 1:
            return count
        n = reduce(lambda x, y: x*y, [int(i) for i in str(n)], 1)
        count += 1

print(persistence(999))    


def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count