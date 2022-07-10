# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 18:43:56 2021

@author: User
"""
import csv
import pandas as pd

archivo1 = pd.read_csv("TSLA.csv",header = 0)
archivo2 = open("analisis_archivo.csv","w")
df = pd.DataFrame(archivo1)
pca = df['Close'].str.extract('(\d+(?:\. \d+)?)')
print(pca)
