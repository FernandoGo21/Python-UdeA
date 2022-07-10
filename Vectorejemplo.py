# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:33:30 2021

@author: User
"""
import random
class vector:
    def __init__(self, n):
        self.n = n
        self.V = [0]*(n+1)
    
    def construyevector(self, m, rango):
        self.V[0]= m
        for i in range(1, m + 1):
            self.V[i] = random.randint(1,rango)
        
v1 = vector(5)
v1.construyevector[3,10]

        