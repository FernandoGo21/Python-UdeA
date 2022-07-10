# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:09:12 2021

@author: User
"""

import pandas as pd
# In[]
a = [1,7,2]
b = pd.Series(a)
print(b)

# In[]
print(b[0])

# In[]
a = [1,7,2]
mivar = pd.Series(a, index = ["x","y","z"])
print(mivar)

# In[]
calorias = {"day1":420, "day2":380, "day3":390}
c = pd.Series(calorias)
print(c)
# In[]
datos = {
    "calorias": [420,380,390],
    "duracion": [50,40,45]    
    }
d = pd.DataFrame(datos)
print(d)
# In[]
print(d.loc[2])
