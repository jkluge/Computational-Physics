# -*- coding: utf-8 -*-

import numpy as np

# function of the net radiated power of a surface - given in the task


def P(A, t0, t1):
    return A*0.6*5.67e-8*(t1**4 - t0**4)


temperatures = np.loadtxt("stalplat.txt")  # load the data matrix
total_power = 0  # accumulator for the total power
for i in temperatures:  # loop over all values
    for j in i:
        # accumulate the power, 1/100 of 1m^2 is 0.01 m^2
        total_power += P(0.01, 300, j)
total_power *= 2  # both sides emit power, so we double
print(total_power)
