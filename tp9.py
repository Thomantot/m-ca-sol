# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 21:54:19 2023

@author: User
"""
import numpy as np
from scipy.optimize import fsolve

import numpy as np
def q1():
    E = 205000
    v = 0.3
    G = E/(2*(1+v))
    
    d = 862
    e = 1.37
    p = 0.98
    
    
    a = (d-e)/2
    b = (d+e)/2
    
    
    u = 1/(2*G*(b*b-a*a)) * (  (1-2*v) * (a*a*p)*d/2 + a*a*b*b*p*2/d)
    return 2*u

def q2():
    
    p = 18.09
    a = 632
    r = 1.646*1000
    
    sMax =   p*(a*a)/(r*r)
    return sMax

def q3():
    rho = 2800
    w = 851
    nu = 0.33
    G = 26300*1000000
    R = 100.14*(0.001)
    
    Ur_R = - ((1-2*nu)/(16*G*(1-nu))) * rho*(w*w)*(R*R*R - (3-2*nu)*R*R*R)
    
    DSection = (np.pi*(R+Ur_R)*(R+Ur_R)) - (np.pi*R*R) 
    return DSection*1000000


########################################
########################################
def q2():
    
    

    R = 12*1000
    nu = 0.37;
    G = 26.6 *1000
    g = 0.001;
    gamma = 1.237 * 0.000001
    
    
    A = (1- 2*nu)* gamma*g / (2*G*(1-nu)*R)
    C1 = 3*A*(R*R)*(nu-3)/(10*(1+nu))
    
    ur_R = (A*R*R*R)/10 + C1*R/3
    
    VarV = (4/3)*np.pi*(R+ur_R)*(R+ur_R)*(R+ur_R) - (4/3)*np.pi*R*R*R 
    return VarV
    
def q3():

    E = 205000
    nu = 0.3
    Pmax = 550.73
    C1plusC2 = 0.275
    k1 = (1 - nu**2)/(np.pi*E)
    k2 = k1
    
    def f(P):
        return P - (2/3)*Pmax*(np.pi*( (3*np.pi/4)*P*(k1+k2)/(C1plusC2))**(2/3))
    
    P = fsolve(f, [0, 1000]) # définition d'une valeur initiale
    print(P) # afficher les deux solutions 
def q4():
    
    
    R = 116.44
    r = 5.81
    t = 37.56*(2*np.pi/360)
    L = 1
    D = 14.03
    
    R1_1 = -(R - r)
    R1_2 = r
    R2_1 = D/2
    
    C2moinsC1 = 0.5*np.sqrt( ((1/R1_1) - (1/R1_2))**2 + (1/R2_1)**2 + 2*((1/R1_1) - (1/R1_2))*(1/R2_1)*np.cos(2*t) )
    # de l'odre de 10^-2
    
    print(C2moinsC1)

