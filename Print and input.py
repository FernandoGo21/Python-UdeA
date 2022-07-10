# -*- coding: utf-8 -*-
"""
Created on Sat May 22 08:20:32 2021

@author: User
"""
Nombre = "Luis"
Apellido = "Gomez"
Edad = "22"
Ciudad = "Bogota"
Programadeestudio = "Fundamentos de programacion"
print("PRIMERA FORMA")
print("Nombre = Luis Fernando Gomez Narvaez \nedad = 22\nCiudad = Bogota\nPrograma de estudio = Fundamentos de programacion")
print("     ")
print(Nombre,Apellido,'\n',Edad,'\n',Ciudad,'\n',Programadeestudio)
nombre = input("Escriba su nombre\n")
apellido = input("Escriba su apellido\n")
edad = int(input("Escriba su edad\n"))
ciudad = input("Escriba su ciudad\n")
programadeestudio = input("Escriba el programa que estudia\n")
print("Su nombre es "+ nombre,'\n',"Su apellido es "+ apellido,'\n',"Su edad es ", edad,'\n',"Su ciudad  es "+ ciudad,'\n',"Su programa de estudio es "+ programadeestudio)

""" casteo: Significa cambiar el tipo de dato, por ejemplo cuando se va a obtener 2 tipos de monto:
            ejemplo
                    monto1 = input("Escriba el monto 1 :") RTA = 10
                    monto2 = input("Escriba el monto 2 :") RTA = 20
                    print(monto1+monto2) RTA = 1020
                    Concatena como si fueran strings debido a que no se casteo en el principio.
                    si se castea quedaria
                    monto1 = int(input("Escriba el monto 1: ")) RTA = 10
                    monto2 = int(input("Escriba el monto 2 :")) RTA = 20
                    print(monto1+monto2) RTA = 30
 """
alto = float(input("Escriba el alto de la habitacion\n"))
ancho = float(input("Escriba el ancho de la habitacion\n"))
area=alto*ancho
print("EL primer lado es: ",alto)
print("El segundo lado es: ",ancho)
print("El area de la habiacion es: ",area)
print("El area de la habiacion es: %0.5f"%area) 
""" Se usa porcentaje al final para agregar la cantidad de decimales"""

tomates = 2500 
papas = 2000
cantidaddekgtomate=float(input("Ingrese la cantidad en kilos de tomates\n"))
cantidaddekgpapa=float(input("Ingrese la cantidad en kilos de papa\n"))
totaltomates = cantidaddekgtomate * tomates
print("El precio del tomate es : ",totaltomates) 
totalpapas = cantidaddekgpapa * papas
print("El precio de la papa es : ",totalpapas) 
Total = totalpapas+totaltomates
print("El costo final es : ",Total) 


