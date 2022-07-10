# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 08:32:01 2021

@author: bebeJefEli
"""
import csv 

def solucion():
    #ESTA ES LA FUNCIÓN A LA QUE LE DEBES GARANTIZAR LOS RETORNOS REQUERIDOS EN EL ENUNCIADO.
    
    with open('MSFT.csv') as csvfile:
        reader = csv.DictReader(csvfile)
    
        date = []
        low = []
        high = []
        media = []
        concepto = []
               
    
        for fila in reader:
            
            date.append(fila['Date'])
            low.append(float(fila['Low']))
            high.append(float(fila['High']))
            
            media.append((float(fila['Low'])+float(fila['High']))/2)
        
        """
        for i in range (len(date)):
            
            media.append((low[i]+high[i])/2)                      
        
        """
        
        with open('analisis_archivo.csv', newline='', mode= 'w') as csvfile:
            campos = ['Fecha', 'Mean-Min-Max', 'Concepto']
            writer = csv.DictWriter(csvfile, fieldnames=campos, delimiter='\t')
 
            writer.writeheader()
            
            for i in range(len(media)):
                
                if media[i]<207:
                    concepto.append("MUY BAJO")
                
                elif media[i]>=207 and media[i]<221:
                    concepto.append("BAJO")
                
                elif media[i]>=221 and media[i]<235:
                    concepto.append("MEDIO")
                
                elif media[i]>=235 and media[i]<249:
                    concepto.append("ALTO")
                    
                elif media[i]>=249:
                    concepto.append("MUY ALTO")               
            
                writer.writerow({'Fecha': date[i], 'Mean-Min-Max': media[i], 
                                 'Concepto': concepto[i]})
        
    lowest_value = min(low)
    indice_menor = low.index(lowest_value)
    date_lowest = date[indice_menor]
    
    highest_value = max(high)
    indice_mayor = high.index(highest_value)
    date_highest = date[indice_mayor]

    return date_lowest, lowest_value, date_highest, highest_value

salida = solucion()


