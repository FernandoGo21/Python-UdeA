# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:41:33 2021

@author: User
"""

x=5
y=6
def variables():
    x=2
    print(x)
variables()
print(x)

def variables2():
    global y
    y=3
    print(y)
variables2()
print(y)