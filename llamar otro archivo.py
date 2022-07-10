# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:16:13 2021

@author: User
"""
#Formas de llamar

import operaciones 
#from operaciones import *
#from operaciones import suma, resta, multi, div

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))

# mostrar suma
print("La suma es : {}".format(operaciones.suma(a,b)))

# mostrar resta
print("La resta es : {}".format(operaciones.resta(a,b)))

# Multiplicacion
print("La multiplicacion es: {}".format(operaciones.multi(a,b)))

# division 
print("La division es: {}".format(operaciones.div(a,b)))