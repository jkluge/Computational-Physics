#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 11:53:12 2026

@author: jkluge
"""

import numpy as np
import scipy.optimize as op

g = 9.8067


def f(x): return 1000 * g * np.pi * x * \
    (x - x**2 / 3) - (g * 700 * 4/3 * np.pi * 1)


print(op.brentq(f, 0, 2))
