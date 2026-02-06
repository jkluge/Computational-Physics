#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 21:22:04 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as op
from scipy import integrate as integrate

A = 1 # we assume in the beginning A = 1
#The radial wave function is given as:
P = lambda r: A * r**2 * np.exp(-r / 4) * (1 - (1 / 4 * r + 1 / 80 * r**2))
P_square = lambda r: np.abs(P(r) ** 2)
r = np.linspace(0, 70000000, 1000)

# Find A - Since the integral does not depend on A, we can take it out.
integral = integrate.quad(P_square, 0, np.inf)
# We find A, so that the integral becomes 1 with A as scalar
A = 1 / np.sqrt(integral[0])
print(A)
print(integrate.quad(P_square, 0, np.inf))
# we find the root of the wave function as:
root = op.brentq(P, 1e-12, 50)
print(root)

# Lets plot the probability and wave function
fig, ax = plt.subplots(2,1)
ax[0].plot(r, P(r), color="b")
ax[0].set_title("Radial Wave Function $P(r)$")
ax[0].set_xlabel("Distance r in a.u.")
ax[0].set_ylabel("$P(r)$")
ax[0].grid(True)

ax[1].plot(r, P_square(r), color='r')
ax[1].set_title("Probability Density $|P(r)|^2$")
ax[1].set_xlabel("Distance r in a.u.")
ax[1].set_ylabel("Probability")
ax[1].grid(True)

plt.tight_layout()
plt.savefig("F4.1.eps", format='eps')
