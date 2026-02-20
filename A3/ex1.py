#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 20:44:18 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

n_mm2 = [255, 270, 285, 305, 320, 350, 385, 415, 450, 480, 510, 545]
hb = [76, 80.7, 85.5, 90.2, 95.0, 105, 114, 124, 133, 143, 152, 162]
# As indicated by spyder, interp1d is deprecated - replace by CubicSpline
# f_1 = interp.interp1d(n_mm2, hb, kind="cubic", fill_value="extrapolate")
f_1 = interp.CubicSpline(n_mm2, hb)

x = np.linspace(230, 600, 1000)
fig, ax = plt.subplots()
ax.plot(x, f_1(x))
ax.plot(n_mm2, hb, "+")
ax.plot([290], f_1(290), "*", color="r")
ax.annotate(r"$ 290 \frac{N}{mm^2}\approx 86.74 HB$", xy=(290, 88),
            xytext=(270, 120), arrowprops=dict(arrowstyle="->", color="k"),)
plt.ylabel("Brinell HB")
plt.xlabel(r"Tensile Failure Limit $[\frac{N}{mm^2}]$")
plt.tight_layout()
plt.savefig("tensile_failure.eps", format="eps")
