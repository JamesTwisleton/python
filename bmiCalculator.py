# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:54:37 2021

@author: tijmen
"""
import sys


height = float(sys.argv[1]) #in meteres
weight = float(sys.argv[2])   #in kg
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
