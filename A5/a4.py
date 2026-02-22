#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 11:57:22 2026

@author: jkluge
"""

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

g = 9.8067  # m / s**2
L = 1


def theta(t, theta):
    # theta[0]' = theta[1]
    # theta[1]' = theta[2] = (-g/L) * np.sin*(theta[0](t))
    return [theta[1], (-g/L) * np.sin(t)*(theta[0])]


sol = []
fig, ax = plt.subplots()

for i in np.linspace(0.1, 1, 10):
    sol.append(integrate.solve_ivp(theta, [0, 10], [
               i, 0], t_eval=np.linspace(0, 10, 500)))

for s in sol:
    ax.plot(s.t, s.y[0])

ax.set_xlabel("Time t in [s]")
ax.set_ylabel("Speed v in [m/s]")
ax.legend()
ax.grid()
