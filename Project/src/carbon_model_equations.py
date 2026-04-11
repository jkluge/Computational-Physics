#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:43:18 2026

@author: jkluge
"""

k12 = 1
k21 = 2

n02 = 0
n2 = 1
xi = 2
gamma = 1

# time t corresponds to the variable these equations depend on
# y is the array that holds the differential equations
def system_of_linear_odes(t, y):
    # y[0]' = y[1]
    y[1] = -k12 * y[1] + k21 * (n02 + xi*(n2-n02)) + gamma - f

    
    