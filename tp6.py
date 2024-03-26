# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:25:24 2023

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import bisect
from numpy.fft import fft, ifft
import random
import math

def q1():
    
    p = 97.03
    
    e2 = 17000/60 * 0.35*30/-0.01 * (0.03 - 60/17000 * 0.45 * p + 0.01/0.35)
    
    e22 = (0.35*0.01*e2/(0.35*30)  )/e2
    

    
    """
    solve(system(sig11=sig21,epsi11*60+epsi21*30=0.03,epsi21=((sig11)/(10925)),epsi11=((1)/(17000))*(sig11+0.45*97.03),epsi22=((−0.35*sig21)/(10925))),{sig11,sig21,epsi21,epsi11,epsi22})
    """
    return e22

def q2():
    
    e = 70000
    v = 0.33
    a = 34.28
    l = 0.061
    
    p = e*l/a
    e2 = v*p/e
    e3 = v*p/e
    return a*a*a-(a + e2*a)*(a-l)* (a + e3*a)

def q3():
    h = 7.99
    a = 6.04
    p = 49.3
    f = 785.3
    
    v = 0.3
    e = 205000
    
    epsi3 = 1/e *(v*p + v*p - 1*f/(a*a))
    return epsi3*h

def q4():
    
    h = 25 - 11.14
    e = -0.01
    return 0.01*h

def q5():
    x = 10.8
    y = 10.2
    e = 17000