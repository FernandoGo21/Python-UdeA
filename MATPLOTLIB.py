# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 21:45:19 2021

@author: User
"""

import matplotlib.pyplot as plt
import numpy as np

# In[]
plt.plot([1,2,3,4])
plt.ylabel('eje y')
plt.xlabel('eje x')
plt.show()

# In[]

fig, ax = plt.subplots()

# In[]
ax.plot([1,2,3,4],[1,4,2,3])

# In[]
plt.plot([1,2,3,4],[1,4,2,3])