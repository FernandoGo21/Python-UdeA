# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 08:16:35 2021

@author: User
"""

class Tienda():
    def __init__(self,nombre,direccion,empleados,tipo,tamano,ide):
        self.nombre = nombre
        self.direccion = direccion
        self.empleados = empleados
        self.tipo = tipo
        self.tamano = tamano
    
    def vender(self):
        print("Se ha hecho una venta")
    def comprar(self):
        print("Se ha hecho una compra")
    def domicilios(self):
        print("Se ha hecho un domicilio")
    def inventario(self):
        print("Se ha hecho un nuevo inventario")
    def info(self):
        print("nombre de la tienda: "+self.nombre)     
           

        
       