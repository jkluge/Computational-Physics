#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 14:12:15 2026

@author: jkluge
"""

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt


def f1(t, z): return t*np.exp(-z)


def f2(t, y):
    # y[0]' = y[1]
    # y[1]' = y[2] = sin(x) - y[0]
    return [y[1], np.sin(t) - y[0]]


sol1 = integrate.solve_ivp(f1, [0, 10], [-2], t_eval=np.linspace(0, 10, 100))
sol2 = integrate.solve_ivp(f2, [0, 10], [0, 0], t_eval=np.linspace(0, 10, 100))
fig, ax = plt.subplots()
ax.plot(sol2.t, sol2.y[0], label="y")
ax.plot(sol2.t, sol2.y[1], label="dy/dt")
ax.set_xlabel("t")
ax.set_ylabel("y")
ax.legend()
ax.grid()
