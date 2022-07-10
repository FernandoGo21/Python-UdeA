# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:31:42 2021

@author: User
"""

def mediana(a,b,c):
    if a < b and b < c or a > b and b > c:
        return b
    elif b < a and a < c or b > a and a > c:
        return a
    elif b < c and c < a or b > c and c > a:
        return c