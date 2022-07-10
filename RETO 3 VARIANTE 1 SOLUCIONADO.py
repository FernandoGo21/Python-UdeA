# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:45:50 2021

@author: User
"""
diccionario = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/"
}
def alfabeto_a_morse(caracter):
    if caracter in diccionario:
        return diccionario[caracter]
    else:
        return ""

def traductor_a_morse(mensaje_a_traducir):
    
    fmensaje_traducido = ""
    caracteramorse = ""
    for caracter in mensaje_a_traducir:
        caracteramorse = alfabeto_a_morse(caracter)
        fmensaje_traducido += caracteramorse + " "
    mensaje_traducido = fmensaje_traducido[:-1]
    print(mensaje_traducido)
    return mensaje_a_traducir
traductor_a_morse(mensaje_a_traducir = input('INGRESE LA FRASE A TRADUCIR: '))
"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
