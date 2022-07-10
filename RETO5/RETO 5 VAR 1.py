# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 08:12:41 2021

@author: User
"""


import csv

def solucion():
   """ archivo1 = pd.read_csv("TSLA.csv",header = 0)
    archivo2 = open("analisis_archivo.csv","w")
    df = pd.DataFrame(archivo1)"""
   with open('TSLA.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        
        date = []
        low = []
        high = []
        concepto = []
        close = []
        
        for row in reader:
            date.append(row['Date'])
            low.append(float(row['Low']))
            high.append(float(row['High']))
            close.append(float(row['Close']))

        with open('analisis_archivo.csv', newline='', mode= 'w') as csvfile:
            campos = ['Fecha', 'Concepto']
            writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter='\t')
            writer.writeheader()
            for i in range(len(close)):
                if(close[i]<200):
                    concepto.append("MUY BAJO")
                elif((close[i]>=200) and (close[i]<300)):
                    concepto.append("BAJO")
                elif((close[i]>=300)and(close[i]<500)):
                    concepto.append("MEDIO")
                elif((close[i]>=500)and(close[i]<600)):
                    concepto.append("ALTO")
                elif(close[i]>=600):
                    concepto.append("MUY ALTO")
                writer.writerow({'Fecha': date[i], 'Concepto': concepto[i]})
                
   lowest_value = min(low)
   indice_menor = low.index(lowest_value)
   date_lowest = date[indice_menor]
    
   highest_value = max(high)
   indice_mayor = high.index(highest_value)
   date_highest = date[indice_mayor]
    
   return date_lowest, lowest_value,date_highest, highest_value
       
salida = solucion()