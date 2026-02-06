#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 16:19:23 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt

forty_int = np.random.randint(1, 11, [40])  # We try out 40 testvalues
print(forty_int)  # Check if it worked correctly

u = np.random.randint(1, 7, [10000])  # Die A
v = np.random.randint(1, 7, [10000])  # Die B
w = u + v  # We simulate the throw of two dice

# Count the number of sevens
svn = 0
for x in w:
    if x == 7:
        svn += 1
prob_svn = svn / 100

print("There are %i sevens in the distribution." % (svn)
      + "The chance to throw a seven is therefore %4.2f percent"
      % (prob_svn))
print("From statistics we know that the chance to throw a seven when" +
      "rolling two dice is 6/36 = 16.667 percent")
# Calculate the mean and standard deviation. Plot it in the legend
mean = np.mean(w)
std_dev = np.std(w)
label = f"$\mu = {mean:.2f}$  $\sigma = {std_dev:.2f}$"
fig, ax = plt.subplots()
ax.hist(w, bins=11, color="c", edgecolor="black", label=label)
plt.xlabel("Throws with two dice")
plt.ylabel("Total amount of the value")
plt.legend()

plt.savefig("F2.2.eps", format="eps")

# ax.tick_params(labelsize=14)
