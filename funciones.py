# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 16:19:18 2021

@author: User
"""

# In[]

print("Bienvenido al curso", "Pedro")
print("Bienvenido al curso", "Juan")
print("Bienvenido al curso", "Alba")
print("Bienvenido al curso", "Lucia")
print("Bienvenido al curso", "Diego")
print("Bienvenido al curso", "Ricardo")

# In[]
def mensaje1(nombre):
    print("Bienvenido al curso", nombre)

# In[]
mensaje1("Juan")

# In[]
def prueba():
    pass

# In[]
def saludoBienvenida():
    print("Hola mundo")

# In[]
saludoBienvenida()

# In[]
def suma(a,b,c):
    resultado = a + b + c
    return resultado

# In[]
o1 = suma(2,3,4)
print(o1)

# In[]
o2 = suma(5,6)
print(o2)

# In[]
saludoBienvenida()
# In[]
### Parámetros indefinidos
def funcion(*params):
    for i in params:
        print(i)
    return params

# In[]
t=funcion(2,3,4,4,"hola")

# In[]
def funcion2(**params):
    for i in params:
        print(f"{i} es {params[i]}")
    return params

# In[]
p = funcion2(i=3,b=4, j="hola", k = "python")

# In[]
### Desempaquetado de parámetros
def suma(a,b):
    return a+b

numeros=[2,4]
print(suma(*numeros))

numeros_dicc={"a":2,"b":4}
print(suma(**numeros_dicc))

# In[]
# Funciones Vacias
def sumar(a,b):
    pass

def restar(a,b):
    pass

def ecuacion():
    a=sumar(2,1)
    b=restar(3,3)
    return a, b

print(ecuacion())

# In[]
# Retornar diferentes elementos
def intento(a,b):
    if a==0:
        return 
    elif a==2:
        return a
    else:
        print("hola")
        
print(intento(2,0))

# In[]
### Variables locales
x=2
def varLocal(a,b):
    x=5
    suma=a+b+x
    print("x= ", x)
    return suma

varLocal(3,5)
print("x=",x)

# In[]
# variables globales
x=2
def varGlobal(a,b):
    global x
    x=5
    suma=a+b+x
    print("x= ", x)
    return suma

varGlobal(3,5)
print("x=",x)