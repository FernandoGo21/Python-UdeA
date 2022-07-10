# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 08:58:15 2021

@author: User
"""

from tiendasuperclase import Tienda
class Productos(Tienda):
    def __init__(self,nombre,tamano,tipo,direccion,empleados,marca,cantidad,ide,ida,precio,descripcion,nom):
        super().__init__(nombre,direccion,empleados,tipo,tamano,ide)
        self.nom = nom
        self.marca = marca
        self.cantidad = cantidad
        self.precio = precio
        self.ida = ida
        self.descripcion = descripcion
    def crear(self):
        print("Ingresar nuevos productos")
    def eliminar(self):
        print("Se elimino un producto")
    def modificar(self):
        print("Se actualizo el inventario")
    def info(self):
        print("nombre del producto "+self.nom)   
    def infotienda(self):
        super().info()
        
p1 = Productos("tiendita","media","supermercado","Calle 56",20,"arroz diana",25,1001,11011,2500,"arroz blanco separado en libra","arroz premium")
p1.info()
print(p1.direccion)
p1.infotienda()

