#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:59:13 2021

@author: yamamotod
"""


#Посчитайте сумму квадратов всех двузначных чисел, делящихся на 9.
#
#При решении задачи используйте комбинацию функций filter, map, sum.
#
#Примечание: на 9 должно делиться исходное двузначное число, а не его квадрат

l2 = sum(map(lambda x: x**2, filter(lambda x: x % 9 == 0,[i for i in range(10,99)])))
print(l2)