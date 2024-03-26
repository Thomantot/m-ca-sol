# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:46:46 2023

@author: User
"""
import numpy as np
import math
def question12():
    M=807.37
    a=33.8
    b=51.87
    
    r = a  # rayon max
    alpha = (b**2 - a**2)**2 - 4*a**2*b**2*(math.log(b/a))**2
    Sigma_theta = (-4*M/alpha)*((-a**2*b**2/r**2)*math.log(b/a) + b**2*math.log(r/b) + a**2*math.log(a/r) + b**2 - a**2)
    return Sigma_theta


def question13():
    Q=148.66
    M=261.94
    L=133.76
    return L*Q-M

def question14():
    import math

    a = 4.43
    d = 7.81
    t = 153.6
    
    sigma = t
    r = d
    sigma_rr = (sigma/2)*(1 - (a**2)/(r**2)) + (sigma/2)*(1 + (3*a**4)/(r**4) - (4*a**2)/(r**2))
    return sigma_rr

def question2():
    Tmax = 40.31
    
    h = 7.56
    
    return -Tmax/(2*h)

def quesion3(): #pas bon
    M = 27.68
    N = 19.69
    h = 22.18
    
    c=-M/(2*np.sqrt(3))
    e=-N*np.sqrt(3)/3 - h*M*(1+3*np.sqrt(3))/6
    return (6*c*h+2*e)*h

def question5():
    X = 8.03
    Y = 6.48
    
    Tsigma = np.array([[0.5*X**2 - X*Y, -X*Y], [-X*Y, -(X**2) + (Y**2)/2]])
    
    Contraintes_principales = np.linalg.eigvals(Tsigma)
    max_contrainte_principale = np.max(Contraintes_principales)
    return max_contrainte_principale

################○

def question32():
    l = 70.54
    L = 219.25
    c = 39.37
    
    return 2*c* l/L

