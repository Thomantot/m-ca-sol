# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:09:04 2023

@author: User
"""
import numpy as np

def q1():
    G = 26300;

    D = 13.21
    L = 384.18
    Z = 119.04
    
    b = D/2
    a_Z = ((D/2)/L)*Z
    
    return G*np.pi*(b*b*b*b - a_Z*a_Z*a_Z*a_Z)/2 

def q2():

    G = 1100
    M = 6000
    a = 10
    b1 = 60
    b2 = 120
    l = 800
    
    X = 1.47
    Y = -14.86
    Z = 181.53

    
    b_Z =b2 +((b1-b2)/l)*Z
    THETA_Z = M/ (G*b_Z*(a*a*a)/3)
    return 2*G*THETA_Z*X
def q3():
    X=2.6
    Y=-2.71
    Z=3450
    
    R=np.sqrt(X*X+Y*Y)
    
    return 78800*(2.482*0.000001)*R

def q4():
    
    C=736.38
    L=0.91522
    M=83.8
    teta=(M/C)*(180/np.pi)
    return teta*L/2

def q5():

    C = 925.34 * 0.000001
    M = 90.41 * 0.001
    L = 888.35
    
    
    THETA = (M/C)
    Psi_Ldemi = THETA * L/2 
    return Psi_Ldemi *(360/(2*np.pi))/1000000