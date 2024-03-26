# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:24:33 2023

@author: User
"""

def q1_1():
    l = 118.94
    b = 9.54
    a = 8.49
    v = 0.3
    r = 718.24
    Aire_i = l*2*b
    Ex = -a/r
    Ez = v*a/r
    
    Aire_f = (l + l*Ex)*(2*b + 2*b*Ez) 
    
    return Aire_f - Aire_i

def q2_1():
    
    E = 210000
    r = 524.36
    a = 7.93
    b = 7.8
    
    M = E/r * 4/3 * a*a*a*b
    return M

def q3_1():
    h = 34.5
    v = 0.25
    E = 10.672*1000000000
    g = 9.81
    ro = 1839
    gamma = ro * g
    G = E/(2*(1+v))
    u1 = h*h/2 * gamma*(2*v-1)/(2*G*(1-v))
    return u1

def q5_1():
    gamma = 1860*9.81
    x = 15.03
    v = 0.22
    sig11 = - gamma * x/1000000
    sig22 = - gamma*x*v/(1-v)/1000000
    (sig11 + sig22)/2
    return (sig11 + sig22)/2