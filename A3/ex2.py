#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 22:45:39 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f(A, L):
    return A[0]*L**A[1]


def diff(A, l_measured, t_measured):
    return t_measured - f(A, l_measured)


data = np.loadtxt("pendulum.txt")
# print(data)

l_measured = data[0:, 0]
t_measured = data[0:, 1] / 10
l = np.linspace(0, 50, 200)
A0 = [2, 0.5]
A, q = optimize.leastsq(diff, A0, (l_measured, t_measured))
print("The parameters are:", A)

t_1s = optimize.brentq((lambda x: f(A, x) - 1), 0.1, 50)
print("A string needs to be %4.2f cm long to achieve a period of 1s" %
      (t_1s))
fig, ax = plt.subplots()
ax.plot(l_measured, t_measured, "+", ms=15)
ax.plot(l, f(A, l))
plt.xlabel(r"Length in $[cm]$")
plt.ylabel(r"Period $T$ in $[s]$")

plt.savefig("pendulum.eps", format="eps")
