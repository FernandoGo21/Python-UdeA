# -*- coding: utf-8 -*-
"""
Created on Fri May 28 20:13:34 2021

@author: User
"""
# In[]
lista1 = [5,6,7,0,"hola", True]
print(lista1[0])
print(lista1[-2])
# In[]
lista2 = [1,2,3,["python",False]]
print(lista2[3][0])
# In[]
lista3 = [1,2,3,["python",False,["cadena",5]]]
print(lista3[3][2][0])
# In[]
lista4 = [1,2,3,["python",False,["cadena",5]]]
print(lista3[3][2][0])
# In[]
lista5 = []
variable = input("Ingrese nombre: ")
lista5.append(variable)
print(lista5)
# In[]
lista6 = [1,2,3,[lista2]]
print(lista6)
del lista6[3]
print(lista6)

# In[]
#tuplas
tupla1 = (1,2,3,(9,8))
print(tupla1)
print(tupla1[3][1])
# In[]
dic1 = {"nombre": 'Fernando',"edad":{"25"}}
print(dic1)

