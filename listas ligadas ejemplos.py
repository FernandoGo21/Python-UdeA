# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 08:32:51 2021

@author: User
"""

""" 
Ejemplo de listas ligadas
"""
from lista_ligada import LSL, nodoSimple

nodo1 = nodoSimple("Manzanas")
nodo2 = nodoSimple("Peras")
nodo3 = nodoSimple("Bananos")
nodo4 = nodoSimple("Fresas")
print(nodo1.dato)

# Asignando liga
nodo1.asignarLiga(nodo2)
nodo2.asignarLiga(nodo3)
nodo3.asignarLiga(nodo4)

nuevaliga = nodo1.liga
while not nuevaliga == None:
    print(nuevaliga.dato)
    nuevaliga = nuevaliga.liga
    
# In[]
nodin = nodoSimple("A")
nodofin = nodoSimple("Z")

lista=LSL()

lista.primero=nodin
lista.ultimo=nodofin

print("Lista")
print("Dato del primero nodo: ",lista.primero.dato)
print("Dato del segundo nodo: ",lista.ultimo.dato)
print("Liga del primer nodo: ",lista.primero.liga)
print("Liga del segundo nodo: ",lista.ultimo.liga)

# In[]
lista_2 =LSL()

lista_2.agregarDato("A")
lista_2.agregarDato("Z")
print("Lista")
print("Dato del primero nodo: ",lista_2.primero.dato)
print("Dato del segundo nodo: ",lista_2.ultimo.dato)
print("Liga del primer nodo: ",lista_2.primero.liga)
print("Liga del segundo nodo: ",lista_2.ultimo.liga)

# In[]
"""
Uso de listas
"""

empleados = LSL()
print(empleados.esVacia())
empleados.agregarDato("Francisco")
empleados.agregarDato("John")
empleados.agregarDato("Eliana")
empleados.agregarDato("Victoria")

empleados.recorrerLista()
empleados.longitud()
print()
print(empleados.esVacia())

# In[]
"""
Borrar datos en posicion especifica
"""

y = nodoSimple()
x = empleados.buscarDato("John",y)
empleados.borrar(x,y)
empleados.recorrerLista()

# In[]
"""
Procedimiento para borrar el primer nodo
"""
print()
x = empleados.primerNodo()
empleados.borrar(x)
print("despues de borrar el primer nodo")
empleados.recorrerLista()
print("\nlongitud: ", empleados.longitud())

# In[]
print()
dat=empleados.ultimo.dato
y = nodoSimple()
x = empleados.buscarDato(dat, y)
empleados.borrar(x, y)
print("despues de borrar la p")
empleados.recorrerLista()
print("\nlongitud: ", empleados.longitud())
    
