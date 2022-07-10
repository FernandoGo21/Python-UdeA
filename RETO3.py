# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 13:01:30 2021

@author: User
"""

equivalencias = {
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
    " ": "/",
}
def caracter_plano_a_morse(caracter):
    if caracter in equivalencias:
        return equivalencias[caracter]
    else:
        # Si no existe, regresamos una cadena vacía
        return ""


def codificar_morse(loop):
    morse = ""
    for caracter in loop:
        caracter_codificado = caracter_plano_a_morse(caracter)
        morse += caracter_codificado + " "
    return morse

def solucion(palabra):
    palabra = input("Ingrese una frase en mayusculas: ")
    print("Codificado:")
    codificado = codificar_morse(palabra)
    print(codificado)
    return codificado

solucion(palabra = "")
