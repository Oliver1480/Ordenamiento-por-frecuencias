# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:21:19 2024

@author: olive
"""

import random
def Frecu(A):
    frec={} #Diccionario que va a almacenar las frecuencias
    for num in A:
        #voy a almacenar una frecuencia cada vez que un numero se encuentre en frec
        frec[num]=frec.get(num,0)+1 #necesito el rango de valores parea mi arreglo
   #quiero la longitud de la lista   
    ## voy a realizar la suma de C desde 1 hasta la longitud de C
    sorted_A=sorted(A,key=lambda x:(-frec[x],A.index(x)))
    return sorted_A
    #requiero la lista ordenada de mi arreglo B:

A=[random.randint(-10,5)for _ in range(100)]#voy a generar un arreglo aleatorio
    
print("Original",A)#CountingSort tendra dos funciones, son ordenar mi lista y las freciencias
#frec={}
sorted_A=Frecu(A)
print("Arreglo final",sorted_A)            