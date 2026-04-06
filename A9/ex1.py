#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:36:34 2026

A program that computes the definite integral from 0 to 10 of xe^{-x}, via
a monte carlo method. 

@author: jkluge
"""
import numpy as np 

# Amount of tries
N_tot = [100, 1000, 10000, 100000, 1000000, 10000000]
def f(x): 
    return x * np.exp(-x)

solution = 1-11*np.exp(-10)

print("The analytical solution of the integral is: %6.8f" %(solution))

for n in N_tot:
    fsum = 0;
    for i in range(n):
        random_x = np.random.rand() * 10
        fsum += f(random_x)
    monte_carlo_solution = 10 * (fsum / n)
    print("For N total = %d, we evaluate the integral as: %10.8f" %(n, monte_carlo_solution))
    print("The error is %6.8f" %(np.abs(solution - monte_carlo_solution)))


