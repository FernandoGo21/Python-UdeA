# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:18:15 2021

@author: User
"""

def multiplicacion(a,b):
    return float(a) * float(b)

def main():
    a = input("Inserte el primer numero: ")
    b = input("Inserte el segundo numero: ")
    resultado = multiplicacion(a,b)
    print(f"La multiplicacion es {resultado}")
    
main()