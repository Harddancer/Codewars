#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:08:22 2021

@author: yamamotod
"""
#Given an array of integers.
#
#Return an array, where the first element is the count of positives 
#numbers and the second element is sum of negative numbers.
#If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):
    count = []
    s = []
    nul = 0
    for i in arr:
        if i > 0:
            count.append(i)
        elif i < 0:
            s.append(i)
        elif i == 0:
            nul += 1
    print(count,s) 
    if   len(arr) == 0:
        count = []
        print(count)       
        return(count)
    
    elif nul == len(arr):
        print([0,0])       
        return([0,0])
    elif   sum(arr) == 0 and sum(count) == 0:
            count = []
            s = []
            print(count,s)       
            return([count,s])
    else:
        print([len(count),sum(s)])       
        return([len(count),sum(s)])
    
    
count_positives_sum_negatives([0,0,0,0,0,0])        




def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
print(count_positives_sum_negatives([0,0,0,0,0,0]))