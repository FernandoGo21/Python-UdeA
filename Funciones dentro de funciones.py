# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:46:26 2021

@author: User
"""

def sumas(a,b):
    def suma1(a,b):
        return a+2*b
    return suma1(2,3)+a+b
sumas(4,5)


def  transmdatos(msg):
    print("Mensaje afuera: ")
    def transmdatos2():
        print(msg)
    transmdatos2()
print(transmdatos("hola, luis"))