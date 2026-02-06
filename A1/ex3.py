#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 00:57:32 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 100)
f = lambda t: 202 * np.exp(-0.42 * t)

t_discrete = np.arange(0, 7)
recorded = (205, 130, 85, 65, 42, 25, 15)

fig, ax = plt.subplots()
ax.plot(t, f(t), label="The measured data points")
ax.plot(t_discrete, recorded, label="$A(t) = 202e^{-0.42t}$")
ax.hlines(y=101, xmin=1.4, xmax=1.8)
ax.annotate("Half-Life at t=1.636y", xy=(1.65, 103), xytext=(2, 150),
    arrowprops=dict(arrowstyle="->", color="k"),)
ax.set_xlabel("Time[y]")
ax.set_ylabel("Radioactivity [kBq]")
ax.grid("on")
ax.legend()

index = np.where(np.isclose(f(t), 101, 1e-2))
print("At t = ", t[index][0],"years the radioactivity halfs to",
      f(t)[index][0],".",)

plt.savefig("F3.1.eps", format='eps')

