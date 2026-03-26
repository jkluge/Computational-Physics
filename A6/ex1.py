#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:00:37 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# The given simplification
GM = 1
# different eccentricities
e = [0, 0.5, 0.9]
# span the linear space
t = np.linspace(0, np.pi * 2, 500)

# initial conditions
x0_0 = 1-e[0]
x0_1 = 1-e[1]
x0_2 = 1-e[2]
x1_0 = 0
y0 = 0
y1_0 = ((1+e[0])/(1-e[0]))**0.5
y1_1 = ((1+e[1])/(1-e[1]))**0.5
y1_2 = ((1+e[2])/(1-e[2]))**0.5


def f(t, y):
    # The system of equations
    # x' =  y[0]' = y[1]
    # x'' = y[1]' = -GM * ((y[0])/(y[0]**2+y[2]**2)**(3/2))
    # y' =  y[2]'   y[3]
    # y'' = y[3]' = -GM * ((y[2])/(y[0]**2+y[2]**2)**(3/2))
    return [y[1], -GM * ((y[0])/(y[0]**2+y[2]**2)**(3/2)), y[3],
            -GM * ((y[2])/(y[0]**2+y[2]**2)**(3/2))]


def energy(x, x1, y, y1):
    # kinetic and potential energy in sum
    return (x1**2+y1**2)/2 - 1/((x**2+y**2)**0.5)


def ang_m(x, x1, y, y1):
    # angular momentum
    return x*y1-y*x1


# Find a solution for the system of linear differential equations and ivs
sol0 = integrate.solve_ivp(
    f, [0, 2*np.pi], [x0_0, x1_0, y0, y1_0], t_eval=t, rtol=1E-8, atol=1E-10)
sol1 = integrate.solve_ivp(
    f, [0, 2*np.pi], [x0_1, x1_0, y0, y1_1], t_eval=t, rtol=1E-8, atol=1E-10)
sol2 = integrate.solve_ivp(
    f, [0, 2*np.pi], [x0_2, x1_0, y0, y1_2], t_eval=t, rtol=1E-8, atol=1E-10)


# fig, ax = plt.subplots()
# ax.plot(sol0.y[0], sol0.y[2], label="$e = 0$")
# ax.plot(sol1.y[0], sol1.y[2], label="$e = 0.5$")
# ax.plot(sol2.y[0], sol2.y[2], label="$e = 0.9$")

# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.legend()
# ax.grid()

# plotting (see previous weeks for more)
fig, ax = plt.subplots(2, 1, sharex=True)

ax[0].plot(t, energy(sol0.y[0], sol0.y[1],
           sol0.y[2], sol0.y[3]), label="Energy e=0")
ax[0].plot(t, energy(sol1.y[0], sol1.y[1], sol1.y[2],
           sol1.y[3]), label="Energy e=0.5")
ax[0].plot(t, energy(sol2.y[0], sol2.y[1], sol2.y[2],
           sol2.y[3]), label="Energy e=0.9")
ax[0].set_ylabel(r"$E[j]$")
ax[0].grid()
ax[0].legend()

ax[1].plot(t, ang_m(sol0.y[0], sol0.y[1],
           sol0.y[2], sol0.y[3]), label="Angular Momentum e=0")
ax[1].plot(t, ang_m(sol1.y[0], sol1.y[1], sol1.y[2],
           sol1.y[3]), label="Angular Momentum e=0.5")
ax[1].plot(t, ang_m(sol2.y[0], sol2.y[1], sol2.y[2],
           sol2.y[3]), label="Angular Momentum e=0.9")
ax[1].set_ylabel(r"$L_z$")
ax[1].set_xlabel("t")
ax[1].grid()
ax[1].legend()


plt.tight_layout()
plt.savefig("ex1_b.eps")
