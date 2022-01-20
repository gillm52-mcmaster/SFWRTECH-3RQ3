# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Name - Manraj Gill
# Student number - 400353744
#This code is from one of my assignments in a course I took. 
import math
import sys
import random

#user input and validation for s0
s0 = int (input('Enter the value of intitial substate concentration:'))

if s0 < 25:
    print("The intitial substate concentration must be between 25 and 75 and a multiple of 5, exiting program")
    sys.exit()
    
elif s0 > 75:
    print("The intitial substate concentration must be between 25 and 75 and a multiple of 5, exiting program")
    sys.exit()

elif s0 % 5 != 0:
    print("The intitial substate concentration must be between 25 and 75 and a multiple of 5, exiting program")
    sys.exit()
    

#user input and validation for mMax
mMax = float (input('Enter the value of maximum specific growth rate:'))

if mMax <= 0.2:
    print("Maximum specific growth rate must be between 0.2 and 0.7, exiting program")
    sys.exit()
    
elif mMax >= 0.7:
    print("Maximum specific growth rate must be between 0.2 and 0.7, exiting program")
    sys.exit()
    
#Printing inputs:
print ("\nThe value of maximum specific growth rate:",mMax)
print ("The value of intitial substate concentration:",s0)

#randon variable ks
ks = random.randint(2, 7)
print("\nThe random variable is:",ks)

#Max dilution rate calculation
dmax = float(mMax * (1 - math.sqrt((ks)/(ks+s0))))
print("The maximum dilution rate is:",format(dmax,'.2f'))

if dmax > 0.35 and dmax < 0.45:
   print("\nKinetic Parameters are acceptable")
else:
   print("\nKinetic parameters are not acceptable")


    

    
    

    
    
 
      
    
    
