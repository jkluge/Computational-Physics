#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:36:48 2026

@author: jkluge
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

e = 1.602e-19
K = 3.477e13
Q = 79
q = 2
v = 1.53e7
t = np.linspace(0, 0.1, 500)

x0_0 = -1e6
# y0_0 = b
x1_0 = v
y1_0 = 0


def f(t, y):
    # x' =  y[0]' = y[1]
    # x'' = y[1]' = K*q*Q * ((y[0])/(y[0]**2+y[2]**2)**(3/2))
    # y' =  y[2]'   y[3]
    # y'' = y[3]' = K*q*Q * ((y[2])/(y[0]**2+y[2]**2)**(3/2))
    return [y[1], K*q*Q * ((y[0])/(y[0]**2+y[2]**2)**(3/2)), y[3], 
            K*q*Q * ((y[2])/(y[0]**2+y[2]**2)**(3/2))]

b_fifty_degrees = [50,0]
for b in range(50, 180, 1):
    sol0 = integrate.solve_ivp(
        f, [0, 0.1], [x0_0, x1_0, b, y1_0], t_eval=t, rtol=1E-8, atol=1E-10)
    a = np.degrees(np.arctan2(sol0.y[3][-1], sol0.y[1][-1]))
    if(b_fifty_degrees[1] < a):
        b_fifty_degrees = [b, a]
        
# b_max = b_fifty_degrees[1]
b_max = 50 # From the solver in Assignment 6, we know this

N_total = 5000 # The total amount of particles
scattering_angles = []
for n in range(N_total):
    by = np.random.uniform(0, b_max)
    bz = np.random.uniform(0, b_max)
    b = np.sqrt(by**2 + bz**2)
    if(b < b_max):
        sol0 = integrate.solve_ivp(
            f, [0, 0.1], [x0_0, x1_0, b, y1_0], t_eval=t, rtol=1E-8, atol=1E-10)
        scattering_angles.append(np.degrees(np.arctan2(sol0.y[3][-1], sol0.y[1][-1])))
    


fig, ax = plt.subplots()
ax.hist(scattering_angles, bins=13, color="plum", edgecolor="black")
ax.set_xlabel(r"Scattering Angle $\theta$ (degrees)")
ax.set_ylabel("Total Amount")
ax.set_title("Histogram of Rutherford Scattering")
plt.tight_layout()
plt.savefig("ex3.eps")
