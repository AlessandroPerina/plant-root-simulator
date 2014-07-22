# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\APerina\.spyder2\.temp.py
"""
from scipy.random import random
import numpy as np
from matplotlib import pyplot as pp

steps = 1000
x=np.zeros([steps])
y=np.zeros([steps])
vx=np.ones([steps])
vy=np.ones([steps])
vabs = np.ones([steps,3])
eta_x = 1
eta_y = 1
for i in range(1,steps):
    vy[i] = abs( vy[i-1] + eta_y*(random(1)-0.5) )
    vx[i] = 0.2*vx[i-1] + eta_x*(random(1)-0.5)
    y[i] = y[i-1] - vy[i]
    x[i] = x[i-1] + vx[i]
    vabs[i:] = sqrt( vx[i]**2 + vy[i]**2 )
    
vabs = vabs / vabs.max()
pp.plot(x,y,'o', markerfacecolor = vabs )

    
    