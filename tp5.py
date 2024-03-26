# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 11:48:29 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import bisect
from numpy.fft import fft, ifft
import random
import math


def f1():
    h = 3.34
    l = 7
    f = 15.73
    return f*l/h

def f2():

    a = 2.3
    l = 8.8
    q = 480

    return q*l/(l-a)

def f5():
    p = 80.3
    l = 4.3
    
    return p*l*l/2

def f3():
    
    f1 = np.zeros(3)
    x1 = np.zeros(3)
    
    f2 = np.zeros(3)
    x2 = np.zeros(3)
    """x = 2,28; y = 8,61 et z = -3,93"""
    
    x1[0] = 2.28
    x1[1] = 8.61
    x1[2] = -3.93
    
    f1[0] = 4.55
    f1[1] = 5.82
    f1[2] = -19.49
    """x = -6,80; y = 8,01 et z = 9,04"""
    x2[0] = -6.8
    x2[1] = 8.01
    x2[2] = 9.04
    
    f2[0] = 8.62
    f2[1] = -7.07
    f2[2] = -9.76


    def déplacement(g):
        g[0] = (0.066*g[0] + 0.087*g[1]) - g[0]
        g[1] = (0.029*g[0] - 0.069*g[1]) - g[1]
        g[2] = - g[2]
        return g
    
    
    x1 = déplacement(x1)
    x2 = déplacement(x2)
    
    w = np.dot(f1,x1) + np.dot(f2,x2)
    return w
        
def f4():
    
    f = np.zeros([3,3])
    f[0,0] = 0.02
    f[0,1] = 0.01
    f[1,0] = 0.076
    f[1, 1] = -0.024
    epsilon = np.zeros([3,3])
    ft = f.transpose()   
    i = np.identity(3)
    epsilon = 0.5*(f + ft) - i
    sigma = np.zeros([3,3])
    sigma[0,0] = 0.76
    sigma[0,1] = 3.91
    sigma[1,0] = 3.91
    sigma[1, 1] = 12.28
    sigma[2,2] = -19.85
    return epsilon*sigma

############
##########
############

def f6():
    p = 408
    a = 2.4
    l = 80
    vb = p*l*0.5 + p*a*(l+a/2)/l - p*a*a*0.5/l
    vbb = p*0.5*(l+2*a)
    
    return vb, vbb

def f7():
    l = 168
    k = 0.649
    f = 16.83
    return f*(l+k*f-l)/2000

def f8():
    h = 8.01
    l = 5
    p = 75
    vb = l*p*3/2
    return vb

def f9():
    a = 3.5
    l = 14.5
    q = 342
    return -q*(a)*0.5

def f10():
    h = 5.08
    l = 5.48
    p = 106.8
    q = 139.2
    va = 0.5*q*l
    return va
        
        
        
        