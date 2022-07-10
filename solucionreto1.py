# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:02:38 2021

@author: User
"""

import random
import math

class vector:
    def __init__(self, n):
        self.n = n
        self.V = [0]*(n+1)
def invierteNumero(n): 
    nunu = 0
    m = n
    while m > 0:
        digito = m % 10
        nunu = nunu * 10 + digito
        m = m // 10
    return nunu
def comienzaCon(x):
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd

n = random.randint(15,30)
s = 0 
vec4 = vector(n)
#Usamos un ciclo para llenar el vector con número del 1 al 99999
for i in range(1, n + 1):
        #Se genera aleatoriamente un número entero entre 1 y 99999"""
        vec4.V[i] = random.randint(1,99999)
        #Se actualiza el valor de la primera posición del vector indicando cuantas posiciones
        #son usadas (En este caso es igual al tamaño del vector)"""
        vec4.V[0] = n
    #Usamos un ciclo para recorrer el vector"""
for i in range(1, vec4.V[0] + 1):
        #En la variable 'nunu' sea almacena el numero invertido de la posición i del vector"""
        nunu = invierteNumero(vec4.V[i])
        #Se pregunta si al invertir el numero sige siendo el mismo(capicua) o si el numero compienza por un dígito par"""
        if vec4.V[i] == nunu or comienzaCon(vec4.V[i]) % 2 == 0:
            #Se realiza la suma de la suma acumulada
           # con el dato en la posición i"""
            s += vec4.V[i] 
  #  """Se retornan los objetos requeridos para efectuar la
    #calificación de la solución"""
print(vec4,s)
