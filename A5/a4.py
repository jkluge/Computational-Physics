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
    return [theta[1], (-g/L) * np.sin(theta[0])]


def theta_analytical(t, theta):
    return theta * np.cos(np.sqrt(g/L) * t)


sol = []
fig, ax = plt.subplots()
t = np.linspace(0, 10, 500)
for i in np.linspace(0.1, 1, 10):
    sol.append(integrate.solve_ivp(theta, [0, 10], [
               i, 0], t_eval=t))
    ax.plot(t, theta_analytical(t, i),
            label=r"$\theta =$ %2.1f" % (i))

for s in sol:
    ax.plot(t, s.y[0])


ax.set_xlabel("Time t in [s]")
ax.set_ylabel("Speed v in [m/s]")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
ax.grid()
plt.tight_layout()
plt.savefig("a4_pendulum.eps")
