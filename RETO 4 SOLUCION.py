# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:40:55 2021

@author: User
"""

def actualizar_estado_editor(operaciones_usuario):
        texto_escrito = []
        texto_actual = ""
        rehacer = []
        cadena_final = ""
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
                        texto_escrito[:-1]
        acu = ""
        for j in range(len(texto_escrito)-1):
            acu = acu + texto_escrito[j]
    
        cadena_final = acu + texto_actual
        return cadena_final


actualizar_estado_editor(operaciones_usuario=["Definamos qué es una función de Python:",
                     "Una función es","un arreglo unidimensional de datos",
                     "DESHACER", "DESHACER", "REHACER", "un grupo de instrucciones"])