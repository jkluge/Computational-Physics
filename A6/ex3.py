#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:00:47 2026

@author: jkluge
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

lambda_0 = np.log(2) / 5.01
lambda_1 = np.log(2) / 138.38
t = np.linspace(0, 100, 500)


def f(t, y):
    # y0' = y[1] = -lambda_0 * y[0]
    # y1' = y[2] = lambda_0 * y[0] - lambda_1 * y[1]
    return [-lambda_0 * y[0], lambda_0 * y[0] - lambda_1 * y[1]]


sol = integrate.solve_ivp(f, [0, 100], [1, 0], t_eval=t)
fig, ax = plt.subplots()
ax.plot(t, sol.y[0], label="$^{210}Bi$")
ax.plot(t, sol.y[1], label="$^{210} Po$")
ax.set_xlabel("Time t in days")
ax.set_ylabel("Amount in mol")
ax.legend()
ax.grid()

plt.tight_layout()
plt.savefig("ex3.eps")
