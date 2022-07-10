# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:00:04 2021

@author: User
"""

# In[]
def funcion(nombre,apellido,ciudad = 'bogota'):
    print(ciudad,nombre,apellido)
    funcion()
    
# In[]
def cuadrado(x):
    return x*x
cuadrado()

# In[]
def intercambio(a,b):
    a,b = b,a
    return a,b
