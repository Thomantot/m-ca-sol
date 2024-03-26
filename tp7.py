# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:36:29 2023

@author: User
"""

import numpy as np

def q1():
    
    f = 265.96
    Epb = 17000
    Eti = 105000
    vpb = 0.45
    vti = 0.34
    epaisseur = 29.73
    l = 24.03
    h = 25.58
    
    s = l*epaisseur*0.5
    
    a = np.array([[s,s, 0], [1/Eti, 0, -1], [0, 1/Epb, -1]])
    b = np.array([f, 0, 0])
    x =  np.linalg.solve(a, b)
    
    
    y = f/(s*Eti/Epb + s)
    
    
    
    return h*y/Epb


def q2():
    
    Vol = np.pi*0.02*0.02*0.06
    e = 17000
    v = 0.45
    h = 2026
    sigma = 1050*9.81*h
    e1 = (1-2*v)*-sigma/e
    
    return 3*e1*Vol

def q3():
    
    f = 182.02
    Epb = 17000
    Eti = 105000
    vpb = 0.45
    vti = 0.34
    epaisseur = 20.34
    l = 30.03
    h = 33.89
    
    a = epaisseur * l
    
    
    
    
    sig = f/a
    e_ti = sig/Eti
    e_pb = sig/Epb
    
    return (e_ti + e_pb)*h/2


def q4():
    
    v = 0.36
    e = 3000
    
    
    l = 219.9
    h = 151.25
    sig1 = 57.82
    sig2 = 19.76
    
    e2 = 1/e * (sig2 - v*sig1)
    
    y = e2*h
    return y


def q5():
    
    e1 = 0.0005
    e2 = -0.0002
    
    v = 0.33
    e = 70000 
    
    e3 = -((1-v)*e1 - v*e2)/v
    return e3
    
def q3b():
    
    f = 26.289
    v = 0.3
    e = 205000 
    return 2*(1+v)*f/e
    
    