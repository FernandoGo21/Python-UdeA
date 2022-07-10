# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:40:08 2021

@author: User
"""
def parametros(*arg):
    for i in arg:
        print(i)
    return arg

def funcion2(**params):
    for i in params:
        print(f"{i} es params{i}")
    return params