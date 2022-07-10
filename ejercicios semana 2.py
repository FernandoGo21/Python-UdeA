# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 15:25:25 2021

@author: User
"""
# In[]
temp = float(input("Ingrese la temperatura en grados Kelvin: "))
f = ((temp-273.15)*(9/5))+32
print("La temperatura en grados farenheit es :",f)

# In[]
"""
Elabore un programa en Python que lea un entero de dos dígitos y produzca como salida los dígitos del número leído con su correspondiente mensaje. Por ejemplo, si el número leído es 27, la salida deberá ser:(sin texto adicional):
2
7
"""
numero = int(input("Ingrese un numero entero de dos digitos :"))
num = str(numero)

    

# In[]
num = int(input("Ingrese un numero entero de dos digitos :"))
num = str(num)
lista = []
for n in num:
    n = int(n)
    lista.append(n)
n1 = lista[0]
n2 = lista[1]
print(n1) 
print(n2)

# In[]
"""
Elabore un programa en Python que lea dos datos enteros correspondiente a los
 lados de un rectángulo e imprima el área y el perímetro.
 """
l1 = int(input("Ingrese el valor del primer lado del rectangulo: "))
l2 = int(input("Ingrese el valor del segundo lado del rectangulo: "))

area = l1*l2
perimetro = 2*l1+2*l2

print("El area del rectangulo es: ",area," y su perimetro es: ",perimetro)

# In[]
"""
Elabore programa en Python que imprima la suma de los números enteros de -200 hasta 600
"""
suma = 0
for i in range(-200,601):
    suma = suma + i
print("la suma de los numeros de -200 hasta 600 es: ",suma)
