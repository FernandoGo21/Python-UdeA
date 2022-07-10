# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:28:39 2021

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
    mensaje_traducido = ""
    caracteramorse = ""
    for caracter in mensaje_a_traducir:
        caracteramorse = alfabeto_a_morse(caracter)
        mensaje_traducido += caracteramorse + " "
    print(mensaje_traducido)
    return mensaje_traducido

traductor_a_morse(mensaje_a_traducir = 'HOLA MUNDO')
"""
Esta línea de código que sigue, permite probar si su ejercicio es correcto
"""
#NO ELIMINAR LA SIGUIENTE LÍNEA DE CÓDIGO
