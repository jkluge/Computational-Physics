#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:00:42 2026

@author: jkluge
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

e = 1.602e-19
K = 3.477e13
Q = 79
q = 2


v = 1.53e7
t = np.linspace(0, 0.1, 500)

x0_0 = -1e6
# y0_0 = b
x1_0 = v
y1_0 = 0


def f(t, y):
    # x' =  y[0]' = y[1]
    # x'' = y[1]' = K*q*Q * ((y[0])/(y[0]**2+y[2]**2)**(3/2))
    # y' =  y[2]'   y[3]
    # y'' = y[3]' = K*q*Q * ((y[2])/(y[0]**2+y[2]**2)**(3/2))
    return [y[1], K*q*Q * ((y[0])/(y[0]**2+y[2]**2)**(3/2)), y[3], K*q*Q * ((y[2])/(y[0]**2+y[2]**2)**(3/2))]


def angle(v, b):
    # The theoretical angle
    return np.degrees(2 * np.arcsin(1/np.sqrt(1+(v**4 * b**2)/(K*Q*q)**2)))


for b in [0, 10, 50, 100]:
    sol0 = integrate.solve_ivp(
        f, [0, 0.1], [x0_0, x1_0, b, y1_0], t_eval=t, rtol=1E-8, atol=1E-10)
    print("The final angle for b = %d is %.f degrees. It should be %f" %
          (b, np.degrees(np.arctan2(sol0.y[3][-1], sol0.y[1][-1])), angle(v, b)))

b = 25
sol0 = integrate.solve_ivp(
    f, [0, 0.1], [x0_0, x1_0, b, y1_0], t_eval=t, rtol=1E-8, atol=1E-10)
print("The final angle for b = %d is %.f degrees. It should be %f" %
      (b, np.degrees(np.arctan2(sol0.y[3][-1], sol0.y[1][-1])), angle(v, b)))

fig, ax = plt.subplots()
ax.plot(sol0.y[0], sol0.y[2], label="Trajectory of particle")
ax.set_xlabel("x[fm]")
ax.set_ylabel("y[fm]")
ax.set_title("Rutherford Scattering Experiment")
ax.legend()
ax.grid()
plt.tight_layout()
plt.savefig("ex2.eps")
