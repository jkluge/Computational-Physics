#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 11:38:24 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt

tol = 0.01
T0 = (650/4)*np.ones((100, 100))  # initialization
T0[0, :] = 100
T0[99, :] = 200  # edge temperatures
T0[:, 0] = 100
T0[:, 99] = 250
T0[30:50, 20:40] = 222.5
T1 = np.copy(T0)  # copy, T1 same edge
diff = tol + 1  # temperature as T0
while diff > tol:
    for i in range(1, 99):  # loop over inner points
        for j in range(1, 99):
            if 30 <= i < 50 and 20 <= j < 40:
                continue
            T1[i, j] = (T0[i+1, j]+T0[i-1, j] +
                        T0[i, j+1]+T0[i, j-1])/4
    diff = np.max(np.abs(T1[1:99, 1:99]-T0[1:99, 1:99]))
    T0 = np.copy(T1)  # T0 copy of T1, not T0=T1
fig, ax = plt.subplots()
plt.title("Heat Simulation")
pos = plt.imshow(T1, cmap="hot")  # plot
cbar = fig.colorbar(pos)
cbar.ax.tick_params(labelsize=14)
plt.savefig("F2.6.eps", format="eps")
