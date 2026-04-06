#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:36:41 2026

@author: jkluge
"""
import numpy as np 

def rho(x): 
    return (2139*x+155)*np.exp(-13.8*x)

radius = 6.96e8 

msum = 0
isum = 0
# use 1 000 000 samples 
for i in range(0,1000000):
    # radial coordinate from zero to one
    x = np.random.rand()
    y = np.random.rand()
    z = np.random.rand() 
    r = (np.sqrt(x**2+y**2+z**2))
    # if the values are within a ball with unit radius, we add to fsum
    if(r <= 1):
        msum += rho(r)
        isum += rho(r) *  ((x*radius)**2 + (y*radius)**2)
    
print("The mass of the sun is: %f"%(8*radius**3 * msum/1000000))
print("The inertia of the sun is: %f"%(8*radius**3*isum/1000000))