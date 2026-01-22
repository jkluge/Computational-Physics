#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 23:05:03 2026

@author: jkluge
"""


#% Import

import numpy as np
import matplotlib.pyplot as plt


#%%Plot a

x = np.linspace(-2, 3)     # Creates 100 values in an array from -2 to 3
y1 = np.exp(-(x)**2)            #
y2 = np.exp(-((x-2)**2))
fig, ax = plt.subplots()
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.plot(x,y1, color="r", label="$f(x)= e^{-x^2}$")
ax.plot(x,y2, color="b", label="$g(x) =e^{-(x-2)^2}$")
ax.legend()
ax.set_title("Plotting two functions in red and blue")
ax.tick_params(labelsize=10)
ax.grid("on")


#%% Plot b


x0 = np.linspace(-2, 1, 100, endpoint=False)
x1 = np.linspace(1+ 1e-14, 2, 100, endpoint = False)  #p.175
x2 = np.linspace(2+ 1e-14, 5, 100)


nominator = lambda x: x**2 - x + 1
denominator = lambda x: (x-1)*(x-2)
f = lambda x: nominator(x) / denominator(x)
fig, ax = plt.subplots()

ax.plot(x0,f(x0), color="b", label="$f(x) = \\frac{x^2 - x + 1}{(x-1)(x-2)}$")
ax.plot(x1,f(x1), color="b")
ax.plot(x2,f(x2), color="b")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_xlim([-2,5])
ax.set_ylim([-20,20])
ax.legend()
ax.annotate('undefined x values', xy=(1, 15), xytext=(1, -4.8), arrowprops=dict(arrowstyle="->", color="k"))
ax.annotate('', xy=(2.1, 15), xytext=(2, -3),
            arrowprops=dict(arrowstyle='->', color='k'))
ax.set_title("Plotting a rational function")
ax.tick_params(labelsize=10)
ax.grid("on")
