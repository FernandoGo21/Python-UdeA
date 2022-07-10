# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:50:04 2021

@author: User
"""

linea = float(input("Ingrese un numero: "))

if ((linea >= 0) and (linea < 10)):
    print("El numero ingresado esta dentro del rango")
else:
    print("El numero ingresado esta fuera del rango")
    
print("El programa se ejecuto correctamente")


linea = float(input("Ingrese un numero: "))

if (linea % 2 == 0):
    print("El numero ingresado es par")
else:
    print("El numero no es par")
print("El programa se ejecuto correctamente")