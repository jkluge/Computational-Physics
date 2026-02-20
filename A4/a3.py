#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 17:17:54 2026

@author: jkluge
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


def rho(r):
    return 0.084 / (1+np.exp(2*r-8))


def q(r):
    return 4 * np.pi * rho(r) * r**2


r = np.linspace(0, 20, 500)
print("The value at 'Infinity' is %e" % rho(r[-1]))  # p.175 1e-14 as limit
fig, ax = plt.subplots()
plt.plot(r, rho(r))
plt.xlabel("$r$ in [fm]")
plt.ylabel(r"Elementary charges  in [q]")

integration_simp = integrate.simpson(q(r), dx=r[1]-r[0])
print(integration_simp)
