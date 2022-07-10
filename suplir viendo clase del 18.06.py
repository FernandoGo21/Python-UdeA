# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:54:12 2021

@author: User
"""

# In[]
"""
Nodo simple 

"""
class Nodo:
    def __init__(self,dato = None, prox = None):
        self.dato = dato
        self.prox = prox
        
    def __str__(self):
        return str(self.dato)
    
v1 = Nodo("Manzanas")
print(v1)
v2 = Nodo("Peras", v1)
print(v2)
v3 = Nodo("Bananos",v2)

# In[]
def VerLista(nodo):
    while nodo:
        print(nodo)
        nodo = nodo.prox

# In[]

    
