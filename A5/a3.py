#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 16:58:58 2026

@author: jkluge
"""

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

v0 = 20  # m/s
m = 100  # kg
g = 9.8067  # m / s**2
k = 40  # Ns**2 / m**2


def v(t, v):
    # v[0]' = v[1] = g - (k/m)*v**2
    return [g - (k/m)*(v**2)]


sol = integrate.solve_ivp(v, [0, 10], [20], t_eval=np.linspace(0, 10, 500))
fig, ax = plt.subplots()

ax.plot(sol.t, sol.y[0], label="v(t)")
ax.set_xlabel("Time t in [s]")
ax.set_ylabel("Speed v in [m/s]")
ax.legend()
ax.grid()
plt.savefig("plot_a3.eps")

print("The terminal velocity is %f m/s" % (sol.y[0][-1]))
