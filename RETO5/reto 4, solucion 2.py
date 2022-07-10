# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 13:04:28 2021

@author: User
"""


operaciones_usuario=["Definamos qué es una función de Python:",
                     "Una función es","un arreglo unidimensional de datos",
                     "DESHACER", "DESHACER", "REHACER", "un grupo de instrucciones"]
"""cadena_final = Definamos qué es una función de Python:Una función esun grupo de instrucciones"""
texto_escrito = []
texto_actual = ""
rehacer = []
acu = ""
for i in range(len(operaciones_usuario)):
    texto_actual = operaciones_usuario[i]
    if((texto_actual != "DESHACER") and (texto_actual != "REHACER")):
        texto_escrito.append(texto_actual)
    if(texto_actual == "DESHACER"):
        rehacer.append(texto_escrito.pop())
        texto_actual = texto_escrito[0]
    if(texto_actual == "REHACER"):
        texto_actual = rehacer.pop()
        texto_escrito.append(texto_actual)
    for i in range(len(texto_escrito)-1):
       acu = acu + texto_escrito[i] + " "
       texto_final = acu
cadena_final = texto_final + texto_actual
print(cadena_final)
        
        