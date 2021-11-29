#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:15:25 2021

@author: yamamotod
"""


#It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.
#
#Return the average of the given array rounded down to its nearest integer.
#
#The array will never be empty.
def get_average(marks):
            summ = sum(marks)
            print(type(summ))
            lens = len(marks)
            lav = summ  // lens
            return lav
            
print(get_average([1,9,3]))