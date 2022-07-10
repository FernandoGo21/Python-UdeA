# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:11:14 2021

@author: User
"""
import numpy as np
import random

# In[]
A = [[1,2],[3,4]]
print(A)

M=[     [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 3, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 2, 0 ],
        [0, 0, 1, 0, 0, 0, 0, 0 ], 
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ]
   ]
print(M[3][1])
# In[]
M1 = np.array([[0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 19, 0, 0 ],
        [0, 3, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 2, 0 ],
        [0, 0, 1, 0, 0, 0, 0, 0 ], 
        [0, 0, 0, 0, 0, 0, 0, 0 ],
        [0, 0, 0, 0, 0, 0, 0, 0 ]
        ])
print(M1[4,6])

# In[]
filas = len(M1)
columnas = len(M1[1])

for i in range(filas):
    for j in range(columnas):
        print(M1[i][j])
        

# In[]        
C = []
for i in range(4):
    C.append([0]*4)

# In[]
import numpy as np
C =np.array([[73, 13,  6,  1, 29],
       [28, 72, 76, 86, 48],
       [94, 18, 32, 24, 33],
       [63, 11, 16, 69, 40],
       [38, 20, 45, 78, 61]])
        
# In[]
sum_diagonal_principal = 0
for i in range(len(C)):
    for j in range(len(C[0])):
        if(i==j):
            sum_diagonal_principal += C[i][j]
print(sum_diagonal_principal)
prod_diagonal_secundaria = 1
for i in range(len(C)):
    for j in range(len(C[0])):
        if(i+j==len(C)-1):
            prod_diagonal_secundaria *= C[i][j]
print(prod_diagonal_secundaria)
modulo = prod_diagonal_secundaria%sum_diagonal_principal
print(modulo)
    
