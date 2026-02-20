#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 16:47:31 2026

@author: jkluge
"""

import numpy as np
import scipy.optimize as op
import scipy.integrate as integrate


def f(x):
    return x**3 * np.sin(x)


x = np.linspace(0, 3, 11)
y = f(x)
n11_trap = integrate.trapezoid(y, dx=x[1]-x[0])
n11_simp = integrate.simpson(y, dx=x[1]-x[0])

print("N=11, Trapezoid, Result: %8.6f" %
      (integrate.trapezoid(y, dx=x[1]-x[0])))
print("N=11, Simpson, Result: %8.6f" % (integrate.simpson(y, dx=x[1]-x[0])))

x = np.linspace(0, 3, 101)
y = f(x)
print("N=101, Trapezoid, Result: %8.6f" %
      (integrate.trapezoid(y, dx=x[1]-x[0])))
print("N=101, Simpson, Result: %8.6f" % (integrate.simpson(y, dx=x[1]-x[0])))
x = np.linspace(0, 3, 201)
y = f(x)
print("N=201, Trapezoid, Result: %8.6f" %
      (integrate.trapezoid(y, dx=x[1]-x[0])))
print("N=201, Simpson, Result: %8.6f" % (integrate.simpson(y, dx=x[1]-x[0])))
