# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:47:33 2023

@author: User
"""

def question11():
    EI=946.82*10**3;
    X=0.831
    p=591.77
    L=4.23
    
    M=p*L**2/2
    V=p*L
    
    D=p/EI*(L**2*X**2/2-L*X**3/2+X**4/6-L**2*X**2/4+L*X**3/3-X**4/8)
    return D*10**3

def question12():
    d1 = 1.002
    d2 = 1.939
    d3 = 0.582
    
    P2 = (39*2)*d2 + 18*d1 + 32*d3
    return P2
def question13():
    E = 70000
    v = 0.33
    t = 7.39
    a = 1.676
    b = 4.658
    c = 4.910
    
    Reponse_1 = t**5/(2*E)*(a**2/3 + a*b/2 + b**2/3 + 2*c**2*(1+v)*t**2/5)
    return Reponse_1
def question14():
    p = 60.42
    L = 10.371
    F = 3*p*L / 16
    return F

def question15():
    L = 15.53e3
    l = 0.6407e8
    A = 96.58e2
    Aprime = 23.48e2
    E = 210000
    nu = 0.3
    
    G = E/(2*(1+nu))
    
    f1 = (L)/(G*Aprime)  # en fait c'est f1/P
    f2 = (L**3)/(3*E*l)  # en fait c'est f2/P
    
    rapport = f1/f2  # pas besoin de connaitre P
    return rapport
