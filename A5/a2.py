#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 14:45:31 2026

@author: jkluge
"""

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt


def f(t, y):
    # y[0]' = y[1]
    # y[1]' = y[0]'' = -2*y[0] + y[2]
    # y[2]' = y[3]
    # y[3]' = y[4] = y[0]-y[2]
    return [y[1], -2*y[0] + y[2], y[3],  y[0]-y[2]]


sol = integrate.solve_ivp(
    f, [0, 20], [10, 0, 15, 0], t_eval=np.linspace(0, 20, 500))

fig, ax = plt.subplots()
ax.plot(sol.t, sol.y[0], label="$y_0$")
ax.plot(sol.t, sol.y[2], label="$y_1$")
ax.set_xlabel("t")
ax.set_ylabel("y")
ax.legend()
ax.grid()

plt.savefig("plot_a2.eps")
