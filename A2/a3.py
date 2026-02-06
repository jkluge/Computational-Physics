#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 17:35:00 2026

@author: jkluge
"""
import matplotlib.pyplot as plt
import numpy as np

dataset = np.loadtxt("co2.txt")
x = np.linspace(2000, 2025, 1357)

fig, ax = plt.subplots()
ax.plot(x, dataset, marker="+", markersize=5)
plt.xlabel("Years from 2000-2025")
plt.ylabel("$CO_2 ~[ppm]$")
plt.savefig("F2.3.eps", format="eps")

min_data = np.min(dataset)
# min_index = np.where(dataset == min_data)
max_data = np.max(dataset)

print("The minimum recorded is %.2f ppm, while the maximum is %.2f ppm" %
      (min_data, max_data))
avg_2000 = np.mean(dataset[0:53])
print("The average in 2000 was %.2f." % (avg_2000))
avg_2025 = np.mean(dataset[1305:1357])
print("The average in 2025 was %.2f." % (avg_2025))
print("Creating a trendline using the mean of 2000 and 2025, "
      + "we can estimate the CO2 concentration for 2050 as %.2f"
      % (avg_2000+2*(avg_2025-avg_2000)))
