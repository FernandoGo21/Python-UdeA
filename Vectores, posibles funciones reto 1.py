# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 20:47:36 2021

@author: User
"""

import operaciones
import random
# 
# In[]
#Empaquetamiento
m = [5, 8, 9, 55, "hola"]

def imprimir(*m):
    for i in m:
        print(i)
        
imprimir(m)

# In[]
#Desempaquetamiento
t = [20, 10]
print(operaciones.suma(*t))
# aqui lo que hace el asterisco es que en la funcion suma del archivo operaciones, el esta esperando un a y un b, dos parametros
#y el esta colocando solo un parametro el cual es t, t es una lista con dos parametros, lo que hace el * es expandir esa lista
# osea se expande la lista, y quedaria 20,10
# In[]
def ingresar_elemento(v,dato):
    v.append(dato)
    return v

ingresar_elemento(t,50)
# In[]
def ingresar_elemento_pos(v,dato,pos):# Seleccionamos vector, dato a cambiar y la posicion del dato
    v.insert(pos,dato) # Cambiar el valor de un datos en cierta posicion
    v[0] += 1 #Se le suma 1 al numero de datos
    return v    
# In[]
#v = vector, n = numero de datos ocupados en el vector, rango = rango de numeros aleatorios
import random
def construyevector(v,n,rango):
    v[0] = n
    for i in range(1,v[0]+1):
        v[i] = random.randint(1,rango)
# In[]
def veclleno(v,n):
    if v[0]==n:
        return True
    return False

# In[]
#Agregar dato
def agregar(v,d,n):
    if veclleno(v,n):
        return False
    v[0] = v[0] + 1
    v[v[0]] = d
    
# In[]
def invertirvector(v):
    v = v[::-1]
    return v

# In[]
def crearvector(tamano):
    vector=[0]*(tamano+1)
    return vector

# In[]
def insertardato(d,i,v,n):
     if veclleno(v,n):
        print("El vector esta lleno")
     for j in range(v[0],i-1,-1):
        v[j+1]=v[j]
     v[i] = d
     v[0] = v[0] + 1
     
# In[]
def imprimevector(v, mensaje = "vector sin nombre \t"):
    print("\n", mensaje, end = ",")
    m = v[0]+1
    for i in range(1,m):
        print(v[i],end = ",")
    print()

# In[]
def datomayor(v):
    mayor = 1
    for i in range(2,v[0]+1):
        if v[i]>v[mayor]:
            mayor=i
    return mayor

# In[]
def datomenor(v):
    menor = 1
    for i in range(2,v[0]+1):
        if v[i]<v[menor]:
            menor=i
    return menor

# In[]
# Detectando varios numeros "menores", que sean iguales
def datomenor1(v):
    menor = 1
    pos = []
    for i in range(2,v[0]+1):
        if v[i] <= v[menor]:
            menor = i
            pos.append(i)
    return pos
# In[]
#Intercambiar
def intercambiar(v, i, j):
    aux = v[i]
    v[i] = v[j]
    v[j] = aux

# In[]
# Formas de intercambiar
def intercambiar2(v,i,j):
    v[i],v[j] = v[j], v[i]

# In[]
def buscardato(v,d):
    i = 1
    while i <= v[0] and v[i] != d:
        i = i + 1
    if i <= v[0]:
        return i
    return -1

    