# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:54:37 2021

@author: tijmen
"""

height = 1.73 #in meteres
weight = 79.6   #in kg
x = (weight/(height**2))

print (x)

if x >= 30:
    print ('obese')
elif x >=25 :
    print ('overweight')
elif x >= 20 :
    print ('normal weight')
elif x >= 15 : 
    print ('underweight')
elif x <= 15 : 
    print ('admit')
