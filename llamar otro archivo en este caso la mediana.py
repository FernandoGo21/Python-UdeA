# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:34:36 2021

@author: User
"""
import mediana

def main():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    c = int(input("Ingrese el tercer valor: "))
    
    print("la mediana es: {}".format(mediana.mediana(a,b,c)))
          
main()
