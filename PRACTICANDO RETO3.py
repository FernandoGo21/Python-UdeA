# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:43:02 2021

@author: User
"""
import numpy as np
A = ".-"
B = "-..."
C = "-.-."
D = "-.."
E = "."
F = "..-."
G = "--."
H = "...."
I = ".."
J = ".---"
K = "-.-"
L = ".-.."
M = "--"
N = "-."
O = "---"
P = ".--."
Q = "--.-"
R = ".-."
S = "..."
T = "-"
U = "..-"
V = "...-"
W = ".--"
X = "-..-"
Y = "-.--"
Z = "--.."
Espacio = "/"
alfabeto = np.array([['A', 'B'],
                     ['C', 'D'],
                     ['E', 'F'],
                     ['G', 'H'],
                     ['I', 'J'],
                     ['K', 'L'],
                     ['M', 'N'],
                     ['O', 'P'],
                     ['Q', 'R'],
                     ['S', 'T'],
                     ['U', 'V'],
                     ['W', 'X'],
                     ['Y', 'Z']])
mensaje = str(input("Ingrese el mensaje a traducir: "))
a = mensaje.split()
palabra1 = []
for i in (a[0]):
        p = i
        palabra1.append(p)


    