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


def f1_sol(t):
    # shifted by 0.25 to show similarity
    return np.log((t**2/2 + np.exp(-2))) + 0.25


def f2(t, y):
    # y[0]' = y[1]
    # y[1]' = y[2] = sin(x) - y[0]
    return [y[1], np.sin(t) - y[0]]


def f2_sol(t):
    return (1/2) * (np.sin(t)-t*np.cos(t)) + 0.25


t = np.linspace(0, 10, 100)
sol1 = integrate.solve_ivp(f1, [0, 10], [-2], t_eval=t)
sol2 = integrate.solve_ivp(f2, [0, 10], [0, 0], t_eval=t)

fig, ax = plt.subplots(2, 1)
ax[0].plot(sol1.t, sol1.y[0], label="y - numerical")
ax[0].plot(t, f1_sol(t),  label="y - analytical")
ax[1].plot(sol2.t, sol2.y[0], label="y - numerical")
ax[1].plot(sol2.t, sol2.y[1], label="dy/dt")
ax[1].plot(t, f2_sol(t),  label="z - analytically")
ax[0].set_xlabel("t")
ax[0].set_ylabel("z")
ax[1].set_xlabel("t")
ax[1].set_ylabel("y")
ax[0].legend()
ax[1].grid()
ax[1].legend()
ax[0].grid()
plt.savefig("a1.eps")