# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 19:28:07 2023

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
    
    Eg = np.zeros([3,3])
    
    Eg[0,1] = 0.01
    Eg[0,2] = -0.09
    Eg[1,0] = 0.01
    Eg[2,0] = -0.09
    Eg[1,1] = 0.06
    
    m = np.zeros([3,1])
    m[0,0] = 1
    n = np.zeros([3,1])
    n[1,0] = 1
    
    mt = m.transpose()
    nt = n.transpose()
    i = np.identity(3)
    Em = np.matmul(mt, np.matmul(Eg, m))
    En = np.matmul(nt, np.matmul(Eg, n))
    
    cos = 1/np.sqrt(1 + 2*Em) * 1/np.sqrt(1 + 2*En) * np.matmul(mt, np.matmul(2*Eg + i, n))
    
    return np.arccos(cos)

def q2():
    """Af ??"""
    
    alpha = 30.8*2*np.pi/360
    ab = 3
    bf = np.tan(alpha)*3
    
    m = np.zeros([2,1])   ## db = m
    m[0,0] = 3
    m[1,0] = -3
    
    m = m/(np.sqrt(9 + pow(3, 2)))
    
    n = np.zeros([2,1])
    n[0,0] = 3
    n[1,0] = -(3-bf)
    n = n/(np.sqrt(9 + pow(n[1,0], 2)))
    mt = m.transpose()
    nt = n.transpose()
    
    Eg = np.zeros([2,2])
    
    Eg[0,0] = 1/18
    Eg[1,1] = -1/18
    Eg[1,0] = 0.4444
    Eg[0,1] = 0.4444
    Em = np.matmul(mt, np.matmul(Eg, m))
    En = np.matmul(nt, np.matmul(Eg, n))
    i = np.identity(2)
    cos = 1/np.sqrt(1 + 2*Em) * 1/np.sqrt(1 + 2*En) * np.matmul(mt, np.matmul(2*Eg + i, n))
    
    return np.arccos(cos)

def q3():
    ad = np.sqrt(pow(3.75, 2) + pow(3.26, 2))
    lambdaa = ad/4
    return 0.5*(pow(lambdaa, 2) -1)

def q4():
    Eg = np.zeros([2,2])
    
    Eg[0,0] = -0.248
    Eg[1,1] = 0.134
    FtF = 2*Eg + np.identity(2)
    return np.sqrt(FtF[1,1])

def q5():
    