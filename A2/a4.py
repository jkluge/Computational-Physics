#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 18:29:51 2026

@author: jkluge
"""

import numpy as np
import matplotlib.pyplot as plt

ccd_matrix = np.loadtxt("CCD.txt")  # load the image
fig, ax = plt.subplots()  # create a plot
ax.imshow(ccd_matrix, cmap="gray", vmin=3, vmax=7)
plt.savefig("F2.4_faulty.png")
for i in range(0, 100):
    for j in range(0, 100):
        if (ccd_matrix[i][j] == 0):  # if faulty, fill in avg of neighbors
            ccd_matrix[i][j] = 1/8*(
                ccd_matrix[i-1][j-1] +
                ccd_matrix[i-1][j] +
                ccd_matrix[i-1][j+1] +
                ccd_matrix[i][j-1] +
                ccd_matrix[i][j+1] +
                ccd_matrix[i+1][j-1] +
                ccd_matrix[i+1][j] +
                ccd_matrix[i+1][j+1])

# plot the matrix as image - the values rank from 3 to 7 - use grayscale
ax.imshow(ccd_matrix, cmap="gray", vmin=3, vmax=7)
plt.savefig("F2.4.png")
