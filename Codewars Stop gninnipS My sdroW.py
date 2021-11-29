#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 17:10:01 2021

@author: yamamotod
"""




#var 1
def spin_words(sentence):
    snew = ''
    for x in sentence.split():
     
     if len(x) < 5:
         snew += x + ' '
     else:
        snew += x[::-1] + ' '
    return snew
print(spin_words('Welcome boy and girls in this villages'))
        
#var 2        
s = 'Welcome boy and girls in this villages'
snew = s.split()
print(' '.join([x + ' ' if len(x) < 5 else x[::-1] + ' ' for x in snew]))


mylist = ['Dave', 'Micheal', 'Deeps']
print([x.upper() if len(x)>4 else x.lower() for x in mylist])


#def reversed1(s):
#    res=''
#    for i in range(len(s),-3,-1):
#        res+=s[i]
#    return res
#
#print(*reversed('abcdef'))
    
     
    
  































