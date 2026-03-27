#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:32:25 2026

@author: jkluge
"""

# based on egensvangning.py - 11.20 in the lecture notes
import numpy as np
import matplotlib.pyplot as plt

n = 3 # number of masses

# generate a diagonal matrix with -2 on the diagonal and 1 adjacent to it. Otherwise zero
A = np.diag([-2] * n) + np.diag([1] * (n - 1), k=1) + np.diag([1] * (n - 1), k=-1)

# find eigenvalues
w, v = np.linalg.eig(A)
# l = pos. in x-led for mass points and end points
l = np.arange(0,n+2) # there are always m+2 line segments.
# largest k
k = np.sqrt(-w[1])
fig, ax = plt.subplots()
counter = 0
for t in np.arange(0,10*np.pi,0.1):
    # u = dist. from equilibrium; dist. is 0 for end points
    u = np.sin(k*t)*np.hstack([0,v[:,1],0])
    ax.plot(l,u,l,u,'o')
    ax.set_ylim([-1,1])
    ax.tick_params(labelsize=14)
    plt.pause(0.1)
    file = "img%i.pdf" %(counter+1) 
    fig.savefig(file)
    counter +=1
    ax.cla() # clear graphical window
    # smallest k
    k = np.sqrt(-w[0])
    fig, ax = plt.subplots()
for t in np.arange(0,10*np.pi,0.1):
    # u = dist. from equilibrium; dist. is 0 for end points
    u = np.sin(k*t)*np.hstack([0,v[:,0],0])
    ax.plot(l,u,l,u,'o')
    ax.set_ylim([-1,1])
    ax.tick_params(labelsize=14)
    plt.pause(0.1)
    file = "img%i.pdf" %(counter+1) 
    fig.savefig(file)
    counter +=1
    ax.cla() # clear graphical window