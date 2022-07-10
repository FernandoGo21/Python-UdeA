# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 09:52:10 2021

@author: User
"""

import Metodos as m

#Crear un vector de tamaño 6 y Luego:
"""
   1. Inicialice 3 elementos con numeros aleatorios entre 1 y 99.
   2. Muestre el vector
   3. Agregue un dato con valor de 69
   4. Imprima nuevamente el vector
   5. Obtenga la ubicación del mayor dato del vector.
   6. Obtenga la ubicación del menor dato del vector.
   7. Imprima un mensaje con las ubicacion del dato mayor y su valor.
   8. Imprima un mensaje con las ubicacion del dato menor y su valor.
   9. Intercambie los elementos mayor y menor.
  10. Imprima nuevamente el vector
  11. Ordenar el vector en orden ascendente
  12. Imprima nuevamente el vector
  13. copie el vector en otro e inviertalo
  14. imprima el nuevo vector
"""
# In[]
#0
v = m.crearVector(6)
# In[]
#1
m.construyeVector(v,3,99)
# In[]
#2
print(v)
# In[]
#3
m.agregarDato(69,v,v)
# In[]
#4
print(v)
# In[]
#5
posmayor = m.mayorDato(v)
# In[]
#6
posmenor = m.menorDato(v)
# In[]
#7
print("El dato mayor esta en la posicion: {}, y su valor es {}".format(posmayor,v[posmayor]))
# In[]
#8
print("El dato menor esta en la posicion: {}, y su valor es {}".format(posmenor,v[posmenor]))
# In[]
#9
m.intercambiar(v,1,3)
# In[]
#10
print(v)
# In[]
#11
m.ordenaAscen(v)
# In[]
#12
print(v)
# In[]
#13
v2 = v.copy()
m.invertir(v2,v2[0])
# In[]
#14
print(v2)


