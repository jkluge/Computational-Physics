# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import os
import cv2


def f(A, t):
    # A second degree polynomial should fit the scenario
    return A[0]*t**2 + A[1]*t+A[2]


def diff(A, t, height_measured):
    # The function to minimize
    return height_measured - f(A, t)


height = []  # The array to collect the height in m
processed_img = []  # collection of processed images - mostly debugging
# The rough RGB of the ball
target = np.array([0, 0.2, 0.16], dtype=np.float32)
tolerance = 0.05
# iterate over the directory with the pictures
for root, dirs, files in os.walk("pics"):
    for file in sorted(files, key=lambda x: int(x[1:-4])):
        if file.endswith(".png"):
            file_path = os.path.join(root, file)
            img = plt.imread(file_path)
            # create a mask, where all values are inside the tolerance
            # ignore red
            img[:, :, 0] = 0
            mask = np.all(np.abs(img - target) <= tolerance, axis=2)
            # create an empty picture to apply the mask on
            result = np.zeros_like(img, dtype=np.float32)
            result[mask] = [1.0, 1.0, 1.0]  # apply masks on empty pictures
            result = cv2.blur(result, (25, 25))  # blur to find clusters
            result = np.mean(result, axis=2)  # convert to greyscale
            processed_img.append(result)
            y, x = np.unravel_index(np.argmax(result), result.shape)
            # from 170 to 1840
            y = 1 - (y-170)/(1840-170)
            height.append(y)

t_discrete = np.linspace(0, 41/50, 41)
t = np.linspace(0, 41/50, 100)
plt.plot(t_discrete, height, "+", label="The collected datapoints")

A0 = [-1, -0.5, 1]
A, q = optimize.leastsq(diff, A0, (t_discrete, height))
print("The coefficient matrix equals %4.2f %4.2f %4.2f" % (A[0], A[1], A[2]))
print("g equals %4.2f" % (2*A[0]))
plt.plot(
    t, f(A, t), label=f"$f(t)={A[0]:0.2f}t^2 + {A[1]:0.2f}t + {A[2]:0.2f}$")
plt.grid(1)
plt.ylabel(r"Height $[m]$")
plt.xlabel("Time $[s]$")
plt.legend()
plt.savefig("plot.eps")
