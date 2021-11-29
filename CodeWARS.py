#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 17:10:01 2021

@author: yamamotod
"""

#
#def number(args):
#    
#    a = ''.join(map(str,args[0:3]))
#    b = ''.join(map(str,args[3:6]))
#    c = ''.join(map(str,args[7:]))
#   
#    
#   
#  
#    print(f'"({a}) {b}-{c}"')
#number([1,2,3,4,5,6,7,8,9,0])
##var 1
#def spin_words(sentence):
#    snew = ''
#    for x in sentence.split():
#     
#     if len(x) < 5:
#         snew += x + ' '
#     else:
#        snew += x[::-1] + ' '
#    return snew
#print(spin_words('Welcome boy and girls in this villages'))        
##var 2        
#s = 'Welcome boy and girls in this villages'
#snew = s.split()
#print(' '.join([x + ' ' if len(x) < 5 else x[::-1] + ' ' for x in snew]))
#
#
#mylist = ['Dave', 'Micheal', 'Deeps']
#print([x.upper() if len(x)>4 else x.lower() for x in mylist])
#
#
#def reversed1(s):
#    res=''
#    for i in range(len(s),-3,-1):
#        res+=s[i]
#    return res
#
#print(*reversed('abcdef'))
#    
#d = 'abcdef'    
#n = d[::-1]
#print(n)      
    
#    
#def solution(a, b):
#    if len(a) < len(b):
#        return(a + b + a)
#    else:
#        return(b + a + b)
#
#print(solution('U','False'))
#
#
#def solution(a, b):
#    return '{0}{1}{0}'.format(*sorted((a, b), key=len))

#
#def get_average(marks):
# 
#   
#            summ = sum(marks)
#            print(type(summ))
#            lens = len(marks)
#            lav = summ  // lens
#            return lav
#            
#print(get_average([1,9,3]))
#def count_positives_sum_negatives(arr):
#    count = []
#   
#    s = []
#    
#    nul = 0
#    
#    for i in arr:
#        if i > 0:
#            count.append(i)
#           
#        elif i < 0:
#            s.append(i)
#            
#        elif i == 0:
#            nul += 1
#  
#    
#    print(count,s) 
#    if   len(arr) == 0:
#        count = []
#        print(count)       
#        return(count)
#    
#    elif nul == len(arr):
#        print([0,0])       
#        return([0,0])
#    
#   
#        
#    elif   sum(arr) == 0 and sum(count) == 0:
#            count = []
#            s = []
#            print(count,s)       
#            return([count,s])
#            
#    
#        
#    else:
#        print([len(count),sum(s)])       
#        return([len(count),sum(s)])
#    
#    
#count_positives_sum_negatives([0,0,0,0,0,0])        
#
#def count_positives_sum_negatives(arr):
#    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
#print(count_positives_sum_negatives([0,0,0,0,0,0]))

#def likes(names):
#
#    l = len(names)
#    if  not names:
#            return f'no one likes this'
#    elif l == 1:
#            return f'{names[0]} likes this'
#    elif l == 2:
#            return f'{names[0]} and {names[1]} like this'
#    elif l == 3:
#            print(len(names))
#            return f'{names[0]}, {names[1]} and {names[2]} like this'
#    else:
#            print(len(names))
#            return f'{names[0]}, {names[1]} and {l-2} others like this'
#
#print(likes(["Alex", "Jacob", "Mark"]))



#test.assert_equals(likes([]), 'no one likes this')
#    test.assert_equals(likes(['Peter']), 'Peter likes this')
#    test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
#    test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
#    test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')


#39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
#999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
#4 --> 0 (because 4 is already a one-digit number)

#Write a function, persistence, that takes in 
#a positive parameter num and returns its multiplicative persistence, which is 
#the number of times you must multiply the digits
# in num until you reach a single digit.
#    test.assert_equals(persistence(39), 3)
#        test.assert_equals(persistence(4), 0)
#        test.assert_equals(persistence(25), 2)
#        test.assert_equals(persistence(999), 4)



#
#def persistence(n):
#    count = 0
# 
#    d = [2,3,4,5,6,7,8,9]
#   
#    if len(str(n)) == 1:
#        count = 0
#        print(count)
#        return count
#    elif len(str(n)) > 1:
#        m = 1
#        while m not in d:
#            for i in str(n):
#                m *= int(i)
#                print(m)
##            l.append(int(n))
##        itog = reduce(mul,l)
#            count += 1
#            print(count,m)
#from functools import reduce
#
#
#def persistence(n):
#    count = 0
#    while True:
#        if len(str(n)) == 1:
#            return count
#        n = reduce(lambda x, y: x*y, [int(i) for i in str(n)], 1)
#        count += 1
#
#print(persistence(999))    


#def persistence(n):
#    n = str(n)
#    count = 0
#    while len(n) > 1:
#        p = 1
#        for i in n:
#            p *= int(i)
#        n = str(p)
#        count += 1
#    return count

#
#Посчитайте сумму квадратов всех двузначных чисел, делящихся на 9.
#
#При решении задачи используйте комбинацию функций filter, map, sum.
#
#Примечание: на 9 должно делиться исходное двузначное число, а не его квадрат

#l = [i for i in range(10,99) if i % 9 ==0]
#l2 = sum(map(lambda x: x**2, filter(lambda x: x % 9 == 0,[i for i in range(10,99)])))
#print(l2)


def add_binary(a,b):
    return str(bin(sum([a,b]))[2:])
   
 
print(add_binary(2,2))



def add_binary(a,b):
    return str("{0:b}".format(a+b))

print(add_binary(2,2))

