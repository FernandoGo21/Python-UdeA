# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:13:19 2021

@author: User
"""

class Circulo:
    pass
c1 = Circulo()
print(type(c1))

#%%
class Circulo:
    
    def __init__(self):
        print("Llamado al constructor")
        
c2 = Circulo()

#%%
class Circulo:
    def __init__(self, radio=1):
        self.radio = radio
        
c3 = Circulo(5)
print(c3.radio)

c4 = Circulo()
print(c4.radio)

#%%
class Circulo:
    def __init__(self,radio=1):
        self.radio = radio
        self.mensaje = "Creacion de la clase"
    
c5 = Circulo(2)
print(c5.mensaje)

# In[]
class Producto2:
    IVA = 0.19
    ENVIO = 1000
    def __init__(self):
        self.nombre = input("Ingrese el nombre del producto: ")
        self.precio = int(input("Ingrese el valor del producto"))
        
    #Metodos
    def precioTotal(self):
        self.total = self.precio + self.IVA*self.precio + self.ENVIO
        return self.total
    
compra3 = Producto2()
print(compra3.precio)
print("El precio total es: ",compra3.precioTotal())

