#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 12:19:12 2026

@author: jkluge
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import integrate
c = 0.25
v = 10
g = 9.81

best_theta = 1
max_t = 0
max_throw = 0


def traj(t, z): return [z[1], -c*np.sqrt(z[1]**2 + z[3]**2)*z[1],
                        z[3], -c*np.sqrt(z[1]**2 + z[3]**2)*z[3] - g]


def position(t, z): return z[2]


# z[2] decreasing with t for  the event to be true,
# the ball should be on its way down
position.direction = -1
position.terminal = True  # integration terminates at event
for i in range(1, 90):
    sol = integrate.solve_ivp(traj, [0, 20], [
                              0, v * np.cos(math.radians(i)), 0,
                              v * np.sin(math.radians(i))], events=position)
    if max_throw < sol.y[0][-1]:
        best_theta = i
        max_t = float(sol.t_events[0][0])
        max_throw = sol.y[0][-1]

sol = integrate.solve_ivp(traj, [0, max_t],
                          [0, v * np.cos(math.radians(best_theta)),
                           0, v * np.sin(math.radians(best_theta))],
                          t_eval=np.linspace(0, max_t, 100))
fig, ax = plt.subplots()
# plot y vs x, i.e. we get a parabola
ax.plot(sol.y[0], sol.y[2])
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.tick_params(labelsize=14)
ax.grid()

print("The longest distance can be achieved with %d degrees throwing angle" % (best_theta))
plt.tight_layout()
plt.savefig("hit_ground.eps")
