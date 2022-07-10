# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:58:23 2021

@author: User
"""

#OTRO EJERCICIO

diccionario={
    "Luis":10,
    "Manzana":2
    }
print(diccionario)

#OTRO EJERCICIO

dic = dict(nombre = 'Luis', apellido = 'Gomez', edad = '22')

#OTRO EJERCICIO
linea = float(input("Ingrese un numero: "))
if linea < 0:
    print("El numero es negativo")
if linea > 0:
    print("El numero es positivo")
if linea == 0:
    print("El numero es cero")
print("El programa se ejecuto correctamente")

#OTRO EJERCICIO

nota = float(input("Ingrese la nota del estudiante: "))
estudiante_matriculado = int(input("Ingrese 1: si el estudiante esta matriculado o 0 si no lo esta: "))
if nota > 2.95:
    if nota <= 5:
        if estudiante_matriculado == 1:
            print("El estudiante aprobo")
        else:
            print("El estudiante no esta matriculado")
    else:
        print("nota no valida")
else:
    print("El estudiante reprobo")
    
print("El programa se ejecuto correctamente")


#OTRO EJERCICIO

linea = float(input("Ingrese un numero: "))

if ((linea >= 0) and (linea < 10)):
    print("El numero ingresado esta dentro del rango")
else:
    print("El numero ingresado esta fuera del rango")
    
print("El programa se ejecuto correctamente")

#OTRO EJERCICIO

linea = float(input("Ingrese un numero: "))

if (linea % 2 == 0):
    print("El numero ingresado es par")
else:
    print("El numero no es par")
print("El programa se ejecuto correctamente")

#OTRO EJERCICIO

Edad = int(input("Cual es su edad :"))
if Edad >= 18:
    print("Bienvenido a la fiesta")
else:
    print("Ingreso no permitido")
print("Ejecucion terminada")

